import pandas as pd
from datetime import datetime
from io import BytesIO
from tempfile import NamedTemporaryFile
import os
import mimetypes
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .excls import read_excel_to_dataframe, get_row_by_cell_id

from .forms import SingUpForm, FormDataForm

from .extraction import ocr_image

# Create your views here.
def home(request):
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = user_name, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged Succefully !")
            return redirect('agroform')
        else:
            messages.success(request, "There Was an Error")
            return redirect('home')
    else:
        return render(request, template_name="formsite/home.html", context={})


def agroform(request):
    submitted = False
    extracted_data = {}

    if request.method == 'POST':
        if 'image' in request.FILES:
            print("in the first")
            uploaded_image = request.FILES['image']
            cell_id = request.POST["cell_id"]
            
            excel_file_path = "all_village_ids_tree disgit.xlsx"  # Replace with the actual path to your Excel file
            sheet_name = 'Samples'  # Replace with the name of the sheet you want to read (if applicable)
            target_cell_id  = int(cell_id)
            df = read_excel_to_dataframe(excel_file_path, sheet_name)
            
            if df is not None:
                specific_row = get_row_by_cell_id(df, target_cell_id)
                if not specific_row.empty:
                    print("Specific row data:")
                    print(specific_row)

                    province = specific_row.iloc[0]['Province']
                    district = specific_row.iloc[0]['District']
                    sector = specific_row.iloc[0]['Sector']
                    cellule = specific_row.iloc[0]['Cell']

                    species = specific_row['spacies'].tolist()
                    species_ = []
                    for i, data in enumerate(species):
                        species_.append((data, data))
                        print(species_)
                        #form.fields["species"].choices = species_

                    initial_Qts =specific_row['Qts'].tolist()
                    initial_Qts_ = []
                    for i, data in enumerate(initial_Qts):
                        initial_Qts_.append((data, data))
                        #form.fields["initial_qts"].choices = initial_Qts_

                    villages = specific_row['Village'].tolist()
                    villages_ = []
                    for i, data in enumerate(villages):
                        villages_.append((data,data))
                        #form.fields["villages"].choices = villages_


                    df = {
                        "province":province,
                        "district":district,
                        "sector":sector,
                        "cellule":cellule,
                        "species":species_,
                        "initial_qts":initial_Qts_,
                        "villages":villages_,
                    }
                    print(df)
                else:   
                    print("No row found for the specified Cell_ID.")
                #print("DataFrame created successfully:")
                #print(df.head())  # Display the first few rows of the DataFrame
            else:
                print("Failed to create DataFrame.")

            # extration of data here
            # populate the data extracted into a python dictionnary
            # Read the uploaded image data and create a BytesIO object
            # Save the uploaded image temporarily
            with NamedTemporaryFile(delete=False) as temp_file:
                for chunk in uploaded_image.chunks():
                    temp_file.write(chunk)
            
            # Pass the temporary file path to ocr_image function
            extracted_data = ocr_image(temp_file.name)
            #extracted_data2 = extracted_data + df
            #print(extracted_data2)
            extracted_data.update(df)
            # image_data = BytesIO(uploaded_image.read())
            # extracted_data = ocr_image(uploaded_image)
            if extracted_data:
                submitted = True
                form = FormDataForm(initial=extracted_data)
                print(extracted_data)
                #extracted_data = {}
            """ 
            if uploaded_image:
                submitted = True
                form = FormDataForm(initial=extracted_data) """
        else:
            form = FormDataForm(request.POST)
            print("in saving")
            print(form.errors)

            if form.is_valid():
                print("valid")
                form.save()

                # save to an excel file
                new_file = "C:/Users/ndeze/OneDrive/Documents/Data.xlsx"
                sheet_name = 'Samples'  # Replace with the name of the sheet you want to read (if applicable)
                existing_df = read_excel_to_dataframe(new_file, sheet_name)
                print(f"existing df : {existing_df}")
                # Get the current date and time
                current_datetime = datetime.now()

                # Convert the datetime object to a string
                current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
                if existing_df is not None:
                    # Create a DataFrame from the form data
                    print([form.cleaned_data["national_id"]])
                    form_data = {
                        "Date": [current_datetime_str],
                        "Names": [form.cleaned_data["names"]],
                        "Date of Birth": [form.cleaned_data["birthdate"]],
                        "Sex": [form.cleaned_data["sex"]],
                        "National ID": [form.cleaned_data["national_id"]],
                        "Phone Number" : [form.cleaned_data["phone_number"]],
                        "Province": [form.cleaned_data["province"]],
                        "District": [form.cleaned_data["district"]],
                        "Sector": [form.cleaned_data["sector"]],
                        "Cell": [form.cleaned_data["cellule"]],
                        "Village": [form.cleaned_data["villages"]],
                        "Species": [form.cleaned_data["species"]],
                        "Qts": [form.cleaned_data["initial_qts"]]
                    }

                    new_df = pd.DataFrame(form_data)
                    if len(existing_df) < 1:
                        new_df.to_excel(new_file,sheet_name=sheet_name, index = True)
                    else:
                        print(f"new df : {new_df}")
                        # Concatenate the existing DataFrame with the new DataFrame
                        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
                        combined_df.to_excel(new_file, sheet_name=sheet_name, index=False)
                        print(f"combined df : {combined_df}")
                        # Write the combined DataFrame back to the specific sheet
                        #with pd.ExcelWriter(new_file, engine='openpyxl', mode='a') as writer:
                        #    combined_df.to_excel(writer, index=False)

                    print("data written")
                    
                
                submitted = False
                # Provide a link to download the generated Excel file
                # return FileResponse(open(excel_path, 'rb'))
                # Provide a link to download the generated Excel file
                # response = HttpResponse(content_type=mimetypes.guess_type(excel_path)[0])
                # response['Content-Disposition'] = f'attachment; filename="{excel_path}"'
                # response.write(open(excel_path, 'rb').read())
                # return response and render(request, 'formsite/agroform.html', {"form": form, "submitted":submitted})
            else:
                print("form not valid")
                #print(form)
    else:
        form = FormDataForm()

    return render(request, 'formsite/agroform.html', {"form": form, "submitted":submitted})

        


    

def logout_user(request):
    logout(request)
    messages.success(request ,"You Have Been Loged out !")
    return render(request, "formsite/home.html", {})
def register(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form .is_valid():
            form.save()

            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # login
            user = authenticate(request, username= username, password= password)

            if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged Succefully !")
                return redirect('agroform')
            else:
                return render(request, 'formsite/register.html', {'form':form})
    else:
        form = SingUpForm()
        return render(request, 'formsite/register.html', {'form':form})
    
    return render(request, 'formsite/register.html', {'form':form})


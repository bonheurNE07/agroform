# AgroForm

AgroForm is a versatile web-based application designed to assist companies in the agriculture sector in Rwanda. However, its functionalities can be adapted and utilized in any other sector of agronomy worldwide. The application provides a streamlined interface for managing agricultural data, including user registration, login, and image upload for data extraction.

## Features

1. **User Authentication**:
   - **Register**: New users can create an account by providing a username, password, email address, first name, and last name.
   - **Login**: Registered users can log in using their username and password.

2. **Image Upload and Data Extraction**:
   - Users can upload images for data extraction purposes.
   - The extracted data is associated with a unique Cell ID.

## Installation

To set up AgroForm on your local machine, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone [https://github.com/bonheurNE07/agroform.git](https://github.com/bonheurNE07/agroform.git)
   cd agroform
   ```

2. **Install Dependencies**:
   Ensure you have Python and Django installed on your machine. Then, install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   Run the following commands to apply migrations and set up the database:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Server**:
   Start the Django development server:
   ```sh
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Register a New Account**:
   - Navigate to the registration page and fill in the required details to create a new account.

2. **Login**:
   - Use your registered username and password to log in.

3. **Upload an Image**:
   - After logging in, navigate to the image upload page.
   - Select an image file and enter the corresponding Cell ID.
   - Click the "Extract" button to upload the image and extract data.

## Contributing

We welcome contributions to enhance the functionality and features of AgroForm. If you'd like to contribute, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Project Description

**AgroForm** is an innovative project aimed at streamlining agricultural data management for companies in the agronomy sector. Developed with the unique needs of Rwandan agricultural enterprises in mind, AgroForm's flexible architecture makes it suitable for use in agronomy sectors worldwide. The application offers a comprehensive suite of features, including secure user authentication, intuitive registration processes, and advanced image upload capabilities for data extraction.

AgroForm empowers agricultural companies by providing them with a robust platform to manage their operations more efficiently. By simplifying data management and extraction processes, AgroForm enhances productivity and decision-making in the agricultural sector.

For more information and to get started with AgroForm, visit our GitHub repos

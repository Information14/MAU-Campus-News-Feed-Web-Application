# Campus News Feed Web Application (Modibbo Adama University Yola) 

## How to Run the Project
1. Clone the repository:
    ```bash
    git clone https://github.com/Information14/MAU-Campus-News-Feed-Web-Application.git
    ```

2. Navigate to the project directory:
    ```bash
    cd News 
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application in your browser at `http://127.0.0.1:8000/maunews/`

## Project Overview
The Campus and News Portal for (Modibbo Adama University Yola) is a web application built using Django, which allows users to view, comment on, and manage campus and news posts. The platform provides functionalities such as login, registration, and content creation, with two primary sections: **News** and **Campus**. Users can interact with the posts, view detailed information, and post comments. 

The application also includes admin interfaces for managing the content, including creating and publishing campus and news posts. Additionally, it offers a registration system for users to sign up and express their interests.

## Features
- **News and Campus Sections:** Separate sections for campus and news posts with user interaction through comments.
- **User Authentication:** Login and registration functionality for both news and campus sections.
- **Content Management:** Admin interfaces to create and manage news and campus posts.
- **Commenting System:** Users can comment on posts, enhancing the interactivity of the platform.
- **Pagination:** Posts are paginated for easy navigation.
- **CKEditor Integration:** Rich-text editing for blog content.

## Languages and Technologies Used
- **Backend:** Python (Django)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL Database 
- **Rich Text Editor:** CKEditor 5
- **Authentication:** Django's built-in user authentication system
- **Form Handling:** Django forms for registration and commenting

## Project Structure
- **views.py:** Contains all the views that handle the logic for rendering templates, processing forms, and interacting with models.
- **models.py:** Defines the data models for the application, including news and campus posts, as well as user login and comment systems.
- **urls.py:** Manages the URL routing for various views in the application.
- **And more, etc..** 



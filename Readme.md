
# Parapharmacy Application

Welcome to the Parapharmacy Application, a modern platform developed using Django for managing and selling pharmaceutical products online, with integrated customer support powered by Dialogflow's chatbot.

## Features

- **Product Management**: Manage pharmaceutical products including their details, prices, and availability.
- **Customer Support**: A chatbot powered by Dialogflow to assist customers with common questions and product inquiries.
- **Order Management**: Users can view, place, and track orders for pharmaceutical products.
- **User Authentication**: Secure user authentication system for customers to sign up, log in, and manage their accounts.
- **Responsive Design**: The application is designed to work seamlessly across various devices, including mobile phones and desktops.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (with optional integration of frontend libraries or frameworks like React)
- **Chatbot**: Dialogflow for chatbot integration
- **Database**: SQLite (default) or PostgreSQL
- **Authentication**: Django’s built-in authentication system
- **APIs**: RESTful API for integrating the chatbot and other services

## Installation

### Prerequisites

1. Python 3.x
2. Django
3. Dialogflow API credentials
4. A database (SQLite or PostgreSQL)

### Clone the Repository

```bash
git clone https://github.com/yourusername/parapharmacy-app.git
cd parapharmacy-app
```

### Set Up Virtual Environment

It's recommended to use a virtual environment for your project.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Database

- For SQLite (default), no further configuration is needed.
- For PostgreSQL, update the `DATABASES` setting in `settings.py` with your PostgreSQL credentials.

Run migrations to set up the database:

```bash
python manage.py migrate
```

### Set Up Dialogflow

1. Create a Dialogflow agent at [Dialogflow Console](https://dialogflow.cloud.google.com/).
2. Get the **Dialogflow API credentials** (service account key JSON file) from the Dialogflow console.
3. Add the JSON file to your project directory and set up environment variables to authenticate the Dialogflow API.

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path_to_your_service_account_key.json"
```

### Start the Development Server

Once everything is set up, run the following command to start the Django development server:

```bash
python manage.py runserver
```

You can access the application at `http://127.0.0.1:8000/` in your browser.

### Testing the Chatbot

To test the Dialogflow chatbot:

1. Start the Django development server.
2. Visit the chatbot interface (can be a frontend page that integrates the chatbot or the admin interface).
3. Interact with the chatbot and ensure it responds correctly to your queries.

## Usage

1. **Manage Products**: Admins can log into the Django admin panel and manage the products in the Parapharmacy store.
2. **Customer Interaction**: The chatbot helps customers find the products they need, answer FAQs, and even help them place orders.
3. **Order Placement**: Users can browse available products, add them to their cart, and proceed to checkout.

## Contributing

We welcome contributions! To contribute to the development of the Parapharmacy application:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Acknowledgments

- [Dialogflow](https://dialogflow.cloud.google.com/) for providing chatbot functionality.
- [Django](https://www.djangoproject.com/) for the web framework.
- [PostgreSQL](https://www.postgresql.org/) for the database system (optional).
  

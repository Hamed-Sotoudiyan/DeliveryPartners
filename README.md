
### Delivery Partners Service
This is a Django-based service that manages delivery partners' information 
including their addresses and coverage areas. 

It provides two views: 

1.NearestPartnerView for finding the nearest partner which the coverage area includes the location.

2.PartnerDetailView for retrieving detailed information about a specific delivery partner.

--------------------------------------------------------------------------------------

## Prerequisites
Before running the service, please ensure that you have the following installed:

Python (version 3.8)

Django (version 4.x)

PostGIS

Docker

Docker Compose

--------------------------------------------------------------------------------------
## Installation
Clone the repository: git clone https://github.com/Hamed-Sotoudiyan/DeliveryPartners.git

Navigate to the project directory: cd DeliveryPartners

Create a virtual environment: python3 -m venv env

Activate the virtual environment:

For Windows: env\Scripts\activate

For macOS/Linux: source env/bin/activate

Install the dependencies: pip install -r requirements.txt

---------------------------------------------------------------------------------------------------

## Configuration
The service requires a few configuration settings. 

Create a .env file in the project directory with the following contents:

SECRET_KEY=your_secret_key_here

DEBUG=True

Replace your_secret_key_here with a secure secret key for your Django application.

------------------------------------------------------------------------------

## Running the Service
To run the service locally, follow these steps:

Start the Docker containers using Docker Compose: docker-compose up -d

Apply the database migrations: python manage.py migrate

Run the Django development server: python manage.py runserver

The service should now be accessible at http://localhost:8000.

----------------------------------------------------------------------------------

## API Endpoints

Nearest Partner:
URL: /partners/nearest/?latitude=<your-latitude>&longitude=<your-longtitude>

Method: GET

Response: JSON object representing the nearest delivery partner

Partner Detail:
URL: /partner/<partner_id>/

Method: GET

Response: JSON object representing the detailed information about the delivery partner

------------------------------------------------------------------------------------------

## Running Tests
To run the tests, make sure you are in the project directory and activate the virtual environment. 
Then run the following command:

python manage.py test

------------------------------------------------------------------------------------------

## Deployment
To deploy the service to a production environment, 

please follow the deployment instructions specific to your hosting provider or platform.

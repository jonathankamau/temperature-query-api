[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/aa140ad57ff6445c9c7d9c41a8d0eea2)](https://app.codacy.com/gh/jonathankamau/temperature-query-api?utm_source=github.com&utm_medium=referral&utm_content=jonathankamau/temperature-query-api&utm_campaign=Badge_Grade_Settings)
[![CircleCi](https://circleci.com/gh/jonathankamau/temperature-query-api.svg?style=svg)](https://app.circleci.com/pipelines/github/jonathankamau/temperature-query-api)
[![Coverage Status](https://coveralls.io/repos/github/jonathankamau/temperature-query-api/badge.svg?branch=main)](https://coveralls.io/github/jonathankamau/temperature-query-api?branch=main)
[![Maintainability](https://api.codeclimate.com/v1/badges/1a97c6de621dc9d1a0e2/maintainability)](https://codeclimate.com/github/jonathankamau/temperature-query-api/maintainability)
![CircleCI](https://img.shields.io/circleci/build/github/jonathankamau/temperature-query-api)
[![PyPI pyversions](https://img.shields.io/badge/Python%20Version-3.9-blue)](https://img.shields.io/badge/Python%20Version-3.9-blue)
# Temperature Query API

Temperature Query is an API tool that allows users to be able to retrieve the maximum, minimum, average and median temperature, in fahrenheit, for a given city and period of time.
## API
- This API contains an endpoint that allows users to retrieve temperature data.
- The user gets to provide two input parameters, the `city` name and the `number of days` for which they want to retrieve the information.
- The temperature data gets called from a third party weather API then from the response object only the maximum, minimum, average and median temperature data for each day gets retrieved.
- Using list comprehensions, the daily temperature gets appended to list data structures and the maximum, minimum, average and median temperature for the days given gets computed.

### Available Endpoint
|HTTP Method   | Endpoint  | Usage |
| ------------- | --------- | --------------- |
|GET| `/api/locations/{city}/?days={number_of_days}` | Get the maximum, minimum, average and median temperature, in fahrenheit, for a given city and period of time|

## Getting started with the API
- The project was built using python 3.9 and the [Django framework](https://www.djangoproject.com/). The API utilizes the [Django Rest Framework](https://www.django-rest-framework.org/) toolkit.
- To run this API on your local machine, you will need to clone this project. You can do so using the following command which you can copy and paste on your terminal:

```
 $ git clone https://github.com/jonathankamau/temperature-query-api.git
 ```

- If you would like to test with a deployed version, you can use the following root URL:

```
https://d2p54l8woftw5f.cloudfront.net/
```

And run the endpoint with it as follows:

```
https://d2p54l8woftw5f.cloudfront.net/api/locations/{city}/?days={number_of_days}
```

### Local Environment Installation

- The project
In order to be able to successfully run this project on your local machine, ensure you have the following prerequisites
#### Prerequisites
- Python 3
- Docker
- A Virtual environment (if running manually) based on python 3 within which you will run the project.
- A Weather API token that you can grab from the [weatherapi](https://www.weatherapi.com/). You will need to create an account in order to obtain the token. After getting the token, you can add it to your environment variables using the variable key [here](/env.example).

### Running using Docker
- Ensure you have Docker installed. You can find information [here](https://www.docker.com/get-started) on how to install Docker on your machine.
- The root folder contains a [Makefile](/Makefile) that handles the container builds and runs for the test and app environments

#### Running tests
- While still in the source folder you can run the following command to run the tests in the test environment:

```
 $ make test
 ```

#### Running the app

- While still in the source folder you can run the following command to run the app in the app environment:

```
 $ make dev
 ```

### Running Manually
If you are running the project manually you will need to do the following:
- Ensure you have setup a virtual environment and you have navigated to that environment on  your terminal.
- Install the requirements using this command:
```
 $ pip install -r requirements.txt
 ```
#### Running tests
- You can then run the tests either using the following command:

    ```
    $ pytest
    ```

- You can use the following command as well:
    ```
    $ python manage.py runserver
    ```

## Deployment 🚀

- The API has been deployed on AWS using the following tools:

    - CodePipeline
    - CodeBuild
    - AWS Elastic Beanstalk
    - Application Load Balancer
    - CloudFront

## Built With:

- Python 3.9
- Django
- Django Rest Framework
- Docker
- AWS

## Author 📚

- Jonathan Kamau
    - [Github Profile](https://github.com/jonathankamau)
    - [Linkedin Profile](https://www.linkedin.com/in/kamaujonathan/)

## License 🤝

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

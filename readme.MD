## Micro Django
A journey through building a django-graphql based micro service.
The repo also explores using [ariadne](https://ariadnegraphql.org/) to build a federated schema.
This is part of a micro service architecture where this handles the doctors service. Other services in this project are the `Patients` and `diagnosis` services.
 To view the code on federation, head over to the [federation](https://github.com/KimaruThagna/micro-django/tree/federation) branch of this repo.
 Major changes will be in executing the schema in `micro_django/schema.py` and types in `gql/types.graphql`
## Tech stack
1. [Django](https://www.djangoproject.com/) for backend and business logic
2. [Ariadne](https://ariadnegraphql.org/) to resolve python/django objects to graphql API
3. [Docker](https://docs.docker.com/get-docker/) and
 [Docker compose](https://docs.docker.com/compose/) for container management and deployment.
4. [Gunicorn](https://gunicorn.org/) To serve Django in a production state
5. [Nginx](https://www.nginx.com/) To act as a reverse proxy for Gunicorn.
 
## Overall Architecture.
**Micro-django** is modelled as a doctors service app. The whole architecture involves 3 micro services
1. [Doctors service](https://github.com/KimaruThagna/micro-django)
2. [Patient's service](https://github.com/KimaruThagna/patient-microservice)
3. [Diagnosis service](https://github.com/KimaruThagna/diagnosis-microservice)

and a final service running [apollo federation](https://www.apollographql.com/docs/apollo-server/federation/introduction/) that allows a client to access all 3 services
via a single data graph by implementing a [gateway](https://www.apollographql.com/docs/apollo-server/federation/gateway/).
The gateway service repo can be found [here](https://github.com/KimaruThagna/hospital-federated)

## Installation and running
A pre requisite to install and run this service is 
having [docker]() and [docker compose]() installed
Once installed, clone this repo into your local machine  and copy the contents of `example.env` into your own `.env` file. 
Change the variables as need be

Navigate to the position of the `docker-compose.yml` file
To spin up the service, run the command
```apex
docker-compose up
```
To access the service via the broswer, log on to [http://0.0.0.0:1337/]() since we are serving the app via NGINX

To view the app from the admin side, access the admin via the url [http://0.0.0.0:1337/admin]() and log in with the superuser credentials created in the `.env` file

## Sample Query
- `get_doctors`
```
{
  doctors
  {
    status
    object{
      license_number
      first_name
      uid
      last_name
      county
      specialization
    }
  }
}
```
- `get_doctor`  use whichever uid will be amongst those retrieved in the first query.
```
{
  doctor(uid:"f6fea0be-20ff-4c12-b0cb-fb32d5512346")
  {
    status
    object
    {
      first_name
      last_name
      specialization
    }
  }
}
```

## Sample mutation
- ``create_doctor``
```
mutation
{
createDoctor{
first_name:"John"
last_name:"Doe"
specialization:"cardiologist"
county:"Nandi"
license_number:"001265789" 
}
status
object
{
uid
last_name
first_name
specialization
}
}


```

-   `update_doctor`

```
mutation
{
updateDoctor{
specialization:"cardiologist"
county:"Lamu"
}
status
object
{
uid
last_name
county
specialization
}
}

```

- `delete_doctor`
```
mutation
{
  deleteDoctor(uid:"f3dc4b5e-000-4b88-82a9-345eed624511")
  {
    status
  }
}
```
- `activate_doctor`
```
mutation
{
  activateDoctor(uid:"f3dc4b5e-111-d455-82a9-345eed624511")
  {
    status
  }
}
```
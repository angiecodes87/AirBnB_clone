AirBnB Clone - Console

Description

This project is an integral part of the ALX Full-Stack Software Engineer
program. It serves as the initial phase in creating a comprehensive web
application, specifically an AirBnB clone. This primary step involves the
development of a custom command-line interface (CLI) for managing data and the
foundation classes for storing this data.

Step 1: Implementing a Command Interpreter (Console)

The core component of this project is a command-line interpreter, written in
Python3, designed for executing CRUD operations (Create, Read, Update, Delete)
on AirBnB objects. These objects include User, City, Review, among others, and
more details about the data models are provided in the subsequent section.

Data Models

This project encompasses seven key data models:

BaseModel:

Attributes: id (generated using the uuid package), created_at (indicating the
object's creation time), updated_at (indicating the object's last update time),
and class (specifying the object's type/model).

User:

Attributes: id, created_at, updated_at, class, first_name, last_name, password,
email.

State:

Attributes: id, created_at, updated_at, class, name.

City:

Attributes: id, created_at, updated_at, class, state_id, name.

Amenity:

Attributes: id, created_at, updated_at, class, name.

Place:

Attributes: id, created_at, updated_at, class, city_id, user_id, name,
description, number_rooms, number_bathrooms, max_guest, price_by_night,
latitude, longitude, amenity_ids (a list of related Amenity.id values).

Review:

Attributes: id, created_at, updated_at, class, place_id, user_id, text.

Usage

To utilize the AirBnB Clone Console:

Execute the console application:

./console.py


You will enter the command-line interface, where you can interact with various
object types, such as User, State, City, Amenity, Place, and Review.

Utilize the following commands to engage with objects:

create: Create an object of the specified type. The object's ID will be
displayed after creation.

create User


update: Modify attributes of an object based on its ID.

update User 123456789 first_name "John"


destroy: Delete an object of the specified type with a given ID.

destroy User 123456789


show: Display comprehensive information about a specific object of a given type.

show User 123456789


all: List all available objects of a particular type or all objects if no
type is specified.

all User


help: Retrieve help information for a specific command or display a list of
all documented commands.

help create


Author

Angela Odhiambo

# Welcome to my SongSpots project!

## Why?

This Web app was something I built because I wished something like it existed. I love listening to music, and when I listen to some songs, they take me back to a certain memory from my life. These memories are associated with the place I was in when they happened, so I wanted to be able to pinpoint the exact (or rough) location I was at when I heard a certain song, and I wanted to be able to describe the memory and what was so memorable about that song at that place and time.

This project also helped me bring together new technologies that I have been teaching myself, and gave me great hands on experience with them. I plan to make this my more "long-term" project, so I will be updating it with different features over time.

## Overview

The application allows a user to create a profile and login. After that, they can add songs to their list, by clicking the location on the Google Maps interface and entering the songs title, artist, the date the memory is from, and a description of the memory. The information is then sent to the database, and they can see their information displayed either by refreshing the page, or by navigating to their page of existing songs. The songs are displayed as points on the map, and the user can hover over them to read their details. The users songs are also displayed in a list (without coordinates) on the side of the page.

## The Deets (Technical Details)

The app was made using an AWS RDS Postgres database instance that was made accessible through a Django API using GraphQL to query the data. The frontend was made using React to display the queried data, along with the Google Maps API component. The application security was done using Django/GraphQL JWT authentication.

### Database: AWS RDS PostgreSQL

I chose to use a relational database for this program because there was no need for a document based system. The data is pretty uniform, as all songs will have mostly the same info, so they could all stick to a relational format. The data and API also rely heavily on relations between tables, so a relational database made the most sense (duh). Using Postgres was an easy choice, since it is becoming the industry standard for relational databases. Hosting the database on AWS was an easy choice to make, as I have experience with it and it's much easier than spinning up a database everytime I turn my computer on. Having the database already on AWS also makes it easier to host the app online in the future.

### Backend: Django, GraphQL, JWT Authentication

GraphQL is pretty rad. Since I've already made a couple of REST APIs in my programming days, I wanted to expand my knowledge, and see what other type of APIs were out there. This naturally led me to GraphQL, which I had heard about before but I hadn't *really* looked at it. Once I did, I said, "Holy cow. This is sweet!". Having the data available, at a single endpoint, to be queried makes the API much mkore efficient, as there is not any unnecessary data fetched, and it also results in less requests having to be sent. For the frontend, it makes things a ton easier, as the queries are more adaptable and can be made to perfectly suit the needs of the frontend, getting exactly the data needed with one request. I think GraphQL will be my go to API now instead of REST.

I used Django and the Graphene library to create the API, since I already had experience with Django. This made it easier to learn and implement a GraphQL API, as everything else was mostly familiar to me. Django also has a very robust User model with authentication, and I wanted to get some experience usiing it to create an application that uses JWT authentication. 

### Frontend: React, GraphQL, Google Maps, JWT Authentication


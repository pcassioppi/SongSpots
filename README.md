# Welcome to my SongSpots project!

## Why?

This Web app was something I built because I wished something like it existed. I love listening to music, and when I listen to some songs, they take me back to a certain memory from my life. These memories are associated with the place I was in when they happened, so I wanted to be able to pinpoint the exact (or close enough) location I was at when I heard a certain song, and I wanted to be able to describe the memory and what was so memorable about that song at that place and time.

This project also helped me bring together new technologies that I have been teaching myself, and gave me great hands on experience with them. I plan to make this my more "long-term" project, so I will be updating it with different features over time.

## Overview

The application allows a user to create a profile and login. After that, they can add songs to their list, by clicking the location on the Google Maps interface and entering the songs title, artist, the date the memory is from, and a description of the memory. The information is then sent to the database, and they can see their information displayed either by refreshing the page, or by navigating to their page of existing songs. The songs are displayed as points on the map, and the user can hover over them to read their details. The users songs are also displayed in a list (without coordinates) on the side of the page.

## The Deets (Technical Details)

The app was made using an Amazon RDS PostgreSQL database instance that was made accessible through a Django API using GraphQL to query the data. The frontend was made using React to display the queried data, along with the Google Maps API component. The application security was done using Django/GraphQL JWT authentication.

### Database

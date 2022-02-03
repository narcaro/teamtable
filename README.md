
# Win Loss Matrix
***
#### Language: Python
#### Modules Used: JSON
#### Files used: table.py, teamstats.JSON

This program reads a JSON file containing win/loss data for a number of teams, parses the data and formats it into an easy to read table.



## Authors

- [@Nick Arcaro](https://github.com/narcaro)


## Lessons Learned

When working with nested for loops, do not move on to the next inner loop without being certain the previous loop will output what you're expecting. I was running the loops periodically throughout making them and wasn't getting any errors so I figured everything was working correctly. Once I thought I was finished I ran the program and noticed a few things were off. Only 1 of the rows was printing the correct amount of values and some of the values in other rows were shifted into the wrong columns. I knew it was most likely a simple error, but the fact that I already had so many moving parts made it that much more challenging to diagnose. It felt like trying to find a loose screw in a plane engine. I had to split apart the loops and test each iteration individually to make sure I was getting the expected result before moving on. If I had taken the time at the beginning to make sure everything was working properly it would've saved a lot of time in the long run.
## Optimizations

The biggest optimization I made between versions was the inclusion of a 2D array when creating the table. In my first version, I was just looping through the JSON file, saving what string I needed at the time then printing it to the console. I knew this wasn't ideal, I was mainly doing it just to figure out the logic needed to extract the neccesary information. I got everything working correctly with this method, but it was kind of mess of if/else statements and I knew it wouldn't scale very well if I wanted to eventually improve on the program and display the data in a GUI. In my next version I split my print method into two. One method created and returned an array of the data elements and the other was strictly meant to print the  array to the console. Now that I had a dedicated print method I can call it whenever and whereever I wanted. More importantly, now that the data was represented in an array I could use array methods. The new method that builds the array is also much cleaner and shorter than what I was previously using to print the table.


[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=3747358&assignment_repo_type=AssignmentRepo)

PROJECT OVERVIEW

The project I proposed was a program that would create a schedule for someone based on the amount of sunlight in the day. The amount of sunlight in the day would come from sunrise-sunset API, and the schedule would be generated from a user's to-do list. My submission is a program that allows a user to add items to a to-do list, check them off, and prints out the final list and times.


PROJECT NARRATIVE

To reach Milestone 1, I only got the basics of the list working. This involved inputs from the user and adding them to lists in a while loop. I reviewed lectures and lessons from code academy to remember how to create a list, add items to them, and work through a loop. To reach Milestone 2, I seperated my code into functions to make my code easier to follow and understand. I also created a new function that allowed a user to check off items. This involved using a for loop to read through the list to find the item, and if statements to determine what to do if the item was found in the list or not. Rewatching the lectures were particularly helpful in figuring out how to do this. For my final submission, I redesdigned the loop to print out a menu that told the user what options they had and what to input. I also fixed the edit_schedule function to also remove the corresponding times from the time list. This seemed difficult, but I was surprised how easy this became when using the "pop" method.
If I were to do this project again, I would want to organize my code more. The loops and functions within the loop became hard to follow. I would also want to create a function that generated the total time that the to-do list would take to complete.


CORRECTIONS

After Milestone 1, you said that you were getting an error, so I added code to make sure that the user's input was always converted to a string (lines 13, 18, 23, 31, 45, 66). You also mentioned giving the user an option to check off items, so I created an if statement (line 15) that would redirect the user to a new function allowing them to check off items (line 42). After Milestone 2, you recommended also removing the to-do list times from the time list when a user removes the corresponging list item. To do this, I created a variable that kept track of where the item was located in the to-do list (line 49), and popped that item from the time list (line 62). You also recommended giving the user a menu showing what options they had in the loop, so I updated those inputs (lines 18, 23).
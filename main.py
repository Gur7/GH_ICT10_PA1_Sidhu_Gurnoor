# Students in different Clubs
from pyscript import display


First_Club = {"Alice", "Bob", "David", "Jose" , "Eve", "Frank"}
Second_Club = {"Jose", "David", "Eve", "Frank", "Grace", "Seo"}

display(First_Club | Second_Club, target="output")
display(First_Club & Second_Club, target="output")
display(First_Club, target="output")
display(Second_Club, target="output")
display(First_Club - Second_Club, target="output")
from pyscript import document, display

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return (
            f"Hello, my name is {self.name}. "
            f"I am in section {self.section}, "
            f"and my favorite subject is {self.favorite_subject}."
        )

classmates = [
    Classmate("Bea",    "Topaz", "ICT"),
    Classmate("Sang",   "Topaz", "Science"),
    Classmate("Allen",  "Topaz", "ICT"),
    Classmate("Ramon",  "Topaz", "Science"),
    Classmate("Simran", "Topaz", "English"),
]

def show_list(event):
    document.getElementById("output").innerHTML = ""
    for mate in classmates:
        display(mate.introduce(), target="output")

def add_classmate(event):
    name = document.getElementById("Name").value.strip()
    section = document.getElementById("Section").value.strip()
    favorite_subject = document.getElementById("FavoriteSubject").value.strip()

    if not name or not section or not favorite_subject:
        display(
            "Fill in all the lines before adding a classmate.",
            target="output",
        )
        return

    new_mate = Classmate(name, section, favorite_subject)
    classmates.append(new_mate)
    display(f"Added: {new_mate.introduce()}", target="output")

    # Clear the input fields after adding
    document.getElementById("Name").value = ""
    document.getElementById("Section").value = ""
    document.getElementById("FavoriteSubject").value = ""
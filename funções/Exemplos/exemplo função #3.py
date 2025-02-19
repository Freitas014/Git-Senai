import random

def generate_stand_name():
    stand_names = ["Crazy Diamond", "Gold Experience", "Star Platinum", "King Crimson", "Sticky Fingers", "Stone Free", "Heaven's Door"]
    return random.choice(stand_names) + " Requiem" if random.random() > 0.8 else random.choice(stand_names)

def generate_protagonist():
    return f"Jo{random.choice(['nathan', 'suke', 'lyne', 'jo', 'elle', 'shiro'])} Joestar"

def generate_antagonist():
    return random.choice(["DIO", "Kars", "Yoshikage Kira", "Diavolo", "Enrico Pucci", "Funny Valentine", "Tooru"])

def generate_arc():
    protagonist = generate_protagonist()
    antagonist = generate_antagonist()
    stand_protagonist = generate_stand_name()
    stand_antagonist = generate_stand_name()
    
    return f"\nARC: {protagonist} vs {antagonist}\n" \
           f"{protagonist} possui o stand {stand_protagonist}, enquanto {antagonist} comanda {stand_antagonist}.\n" \
           f"Uma batalha bizarra está prestes a começar!\n"

def jojo_script():
    while True:
        input("Pressione Enter para gerar um novo arco de JoJo...")
        print(generate_arc())

if __name__ == "__main__":
    jojo_script()




class Member:
    first_name=''
    last_name=''
    blocked_names = ["Lishaa", "Natiniaho", "Israel"]

    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    def get_full_name(self) -> str:
        if self.first_name in Member.blocked_names:
            raise ValueError(f"Name {self.first_name} is not allowed")
        elif self.last_name in Member.blocked_names:
            raise ValueError(f"Name {self.last_name} is not allowed")
        else:
            return f"{self.first_name} {self.last_name}"
    
member = Member("Ahmed", "mohamed")
print(member.get_full_name())
from members.models import Member


def run():
    """Add members to the database."""
    for i in range(10):
        member = Member(
            firstname=f"John {i}",
            lastname=f"Doe {i}",
            phone=1234567890,
            joined_date="2020-01-01",
        )
        print(f"Adding {member.firstname} {member.lastname} to the database.")
        member.save()
    print("Done!")

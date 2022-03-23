from identified_object import IdentifiedObject

class Team(IdentifiedObject):

    # __init__(oid, name)
    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._team_members = []

    # members [r/o prop] -- list of team members
    @property
    def members(self):
        return self._team_members

    # add_member(member) -- ignore request to add team member that is already in members
    def add_member(self, member):
        if member not in self._team_members:
            self._team_members.append(member)

    def remove_member(self, member):
        if member in self._team_members:
            self._team_members.remove(member)

    # send_email(emailer, subject, message) --
    # send an email to all members of a team except those whose email address is None
    def send_email(self, emailer, subject, message):
        members_emails = None
        for x in self.members:
            members_emails.append(x.email)
        emailer.send_plain_email(members_emails, subject, message)

    # __str__() -- return a string like the following: "Team Name: N members"
    def __str__(self):
        return str(self.name + ": " + len(self.members))
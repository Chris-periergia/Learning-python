
Christopher John <christopher.j@hashlogics.com>
Wed, Nov 13, 2024, 12:22 PM
to anomosc@gmail.com

# Real Life Example :

# Create multiple inheritance on teacher,student and youtuber.
# Q. if we have created teacher and now one student joins master degree with becoming teacher then what??

# Ans :  just make subclass from  teacher so that student will become teacher
# Now student is teacher as well as youtuber then what???
# -just use multiple inheritance for these three relations


class teacher:
    def profession_teacher(self):
        print('I am teacher')

class youtuber:
    def profession_youtuber(self):
        print('I am a youtuber')

class student(teacher,youtuber):
    pass

s=student()
s.profession_teacher()
s.profession_youtuber()
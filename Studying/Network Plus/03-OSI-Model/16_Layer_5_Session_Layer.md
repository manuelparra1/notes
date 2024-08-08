Layer Five, the Session Layer.

Now, layer five is our session layer,

and we want to start thinking about what a session is.

The way I like to think about a session

is that it's a conversation that has to be kept

separate from all of the others to prevent

the intermingling of data.

Now, if you think about yourself in a classroom setting,

we might have 20 students sitting here.

Now, if I wanted to ask a question to one student only,

everyone else can listen to it.

Maybe I want to take that student,

and we're going to go walk about in to the hallway

so we can have our own session, our own private

conversation, while all of the other 19 students

can talk among themselves.

And they're having their own session.

That way, we can separate these two sessions apart

and each of us can talk at the same time

without interfering with the other,

me and my student out in the hall

and all the other 19 students sitting back

in the classroom.

Now, that's the idea here when we talk about

the session layer.

We have all sorts of data flying around our networks

all day long, and by establishing these sessions,

we can separate them to prevent the intermingling

or cross-contamination of that data.

Now, what we're going to do is we're going to set up a session,

we're going to maintain a session,

and we're going to tear down a session

here inside the session layer.

Now, what is setting up a session?

This is where we're going to check our user credentials,

and we're going to assign a number to the session

to help identify it.

It's basically some random number

that's going to allow us to negotiate services

for that session with the server

and then negotiate who's going to talk first,

either the server or myself.

Now, let's go back to our classroom setting once more.

If Johnny asks me a question, he says,

hey, professor Dion.

I'll say, yes Johnny?

And then, guess what?

We're going to start talking,

because we've established that session.

I know that Johnny wants to talk to me,

and Johnny knows that I'm ready to talk to him.

Now, I know who he is.

He knows who I am.

And we both know what each other wants.

We want to start talking.

In a computer network, it's a little bit more difficult

but that's really the idea behind it

when we start talking about a session.

Now, the next thing we have to do

is we have to maintain this session.

This is where we're going to transfer data

back and forth across the network

over and over and over again.

Going back to my classroom example,

if Johnny asks me a question, I'd say,

yes, go ahead and ask the question, Johnny.

And then, Johnny's going to ask his question.

And at this point, we're maintaining a session.

So, here we are going back and forth, back and forth,

where I can answer their question

and see if I can answer everything they have for me, right?

Well, the same idea happens here inside our networks.

Now that the session has been established,

we're going to send all of our data back and forth

over and over again.

Now, if we have a break in the connection,

we're going to have to reestablish our connection.

So, for instance, I might say, I'm sorry,

I didn't hear you Johnny.

Can you repeat your question?

Again, I'm maintaining that session.

So, that way, I can get what they want to tell me,

and then I can answer them.

Now, also I'm going to acknowledge the receipt of the data.

I'll say, did you understand my answer, Johnny?

And they'll say, yeah I did.

Or no, I didn't.

And if they did, they'll acknowledge the receipt.

If they didn't, they're going to tell me,

no, I didn't understand.

Can you tell me that again a different way?

Well, the same thing happens digitally with your networks.

And that brings us to the final area.

Tearing down a session.

So, now that the student's question has been answered

in our analogy of the classroom,

I'll say, Johnny, does that answer your question?

And hopefully, he'll say, yes it does.

And at that point, I'll say okay,

we're going to move on to the next thing in the course.

And as I say that,

we're going to move on to the next question.

That tears down the session.

The session between me and Johnny is done,

and I'm going to go back to teaching.

And if Johnny has another question,

he's going to have to raise his hand again,

so that I can go and say, okay Johnny, what's your question?

And we'll start a new session, right?

That would be the end of that particular session

once I answer his question and got confirmation

that he has it.

Then, we can move on.

Now, this is done based on this mutual agreement.

Once we've transferred all the data back and forth

we wanted to, we're going to verify

that I'm ready to tear down the session,

you're ready for the session to be torn down,

and then, we can tear down that session.

The other way we could take down a session

is if one of the parties disconnects

and we simply can't reconnect to them.

For instance let's go back to my classroom example.

Johnny asked a question.

I go on a 30-minute diatribe trying to explain

every possible thing to answer his question.

And I look up and guess what?

Johnny has his head down on the table

and he's fallen asleep.

I bored him to death.

There's no way for me to maintain that session,

because he's not getting the information.

He's completely asleep.

He is dead asleep and he is not listening anymore.

Well, he has disconnected from this conversation.

And therefore, I can't re-engage.

So, I'm just going to stop teaching

and move on to other students who are awake

and are paying attention

and actually have questions for me.

That's the idea here with tearing down a session.

This can be done either mutually

where we both have finished the communication

and we say, yep, I'm done, you're done,

we understand each other.

We move on.

Or the other party simply disappears.

In which case, I want to free up my resources

so I can go help other people again.

And that's what I would do as a computer.

So, what are some examples of Layer 5 devices

or protocols, or things that you should associate

with Layer 5?

Well, the two big ones are H.323 and NetBIOS.

Let's talk about H.323 first.

H.323 is used to set up, maintain, and tear down

voice and video connections.

If you're using FaceTime or Skype

or something like that, you're probably using

something like H.323, which operates

over the RTP or Real-Time Protocol.

Now, I know I just threw out a lot of acronyms for you.

For the exam, if you see something like H.323

or H.264, I want you to think about streaming audio

or streaming video.

Something like FaceTime, Skype, YouTube,

video teleconference, something like that.

These operate over the Real-Time Protocol, known as RTP.

Any time you see RTP, I want you to think about

streaming audio or streaming video.

Generally in a two-way format,

like a phone call or a FaceTime session.

Keep those in your head, and you're going to do great

on the exam cause they do like to throw those in

and I want you to see those.

Now, the second thing I mentioned

is that we have something known as NetBIOS.

Now, NetBIOS is used by computers to share files

over a network.

Windows uses this as the method of its file sharing

as well inside, so you're going to see it a lot

on your networks.

Now, again, when we talk about Layer 5 devices,

there's really not a device necessarily,

but it's more of these protocols and software.

So, if you see something like H.323, RTP, or NetBIOS,

I want you to remember, these are all Layer 5 issues.

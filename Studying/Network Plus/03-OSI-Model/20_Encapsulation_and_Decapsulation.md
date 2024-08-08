Encapsulation and Decapsulation.

In this lesson,

we're going to talk about encapsulation and decapsulation.

Encapsulation is the process of putting headers

and sometimes trailers around some of our data.

Think about it like this.

You just finished writing a letter to your grandma,

and now you want to send it to her.

Well, to do that, you need to put it in an envelope.

Now, when you put the letter in the envelope,

you're actually encapsulating it.

Now, once your grandma gets that envelope,

she wants to be able to read it

and so she has to take the letter out of the envelope

in order for her to read it.

This process is known as decapsulation

because we're removing the encapsulation

that was applied earlier.

Now, I know this is a silly example,

but that's exactly what happens

as we send data on our networks.

It's continually being encapsulated and decapsulated

as it moves up or down the layers of the OSI model.

If we move down the OSI layers, from 7 to 1,

we encapsulate our data.

If we move upward from Layer 1 up to 7,

we decapsulate our data.

So let's take a closer look at how this works

in the real world.

In the OSI model, we use protocol data units or PDUs

to transmit our data.

A protocol data unit is just a single unit of information

transmitted within a computer network.

In the OSI model, they are simply called L,

the layer number, and PDU.

For example, L7 PDU is a Layer 7 PDU.

This type of terminology can be used

for every single layer we have,

but we also have special names for the PDUs

when we reach Layers 1, 2, 3, and 4.

For Layer 1, we call them bits.

For Layer 2, we call them frames.

For Layer 3, we call it packets.

And Layer 4, we call it segments if we're using TCP

or datagrams if we're using UDP.

Now, as a user creates data

and they want to send it over a network,

they're going to enter it into an application

at the application layer, Layer 7.

This data then has a Layer 7 header added

that contains metadata

with the parameters that are agreed upon

by the specific application.

So if you're using HTTP or you're using FTP,

that's going to have specific metadata for that type of data.

Then that information is going to be passed down to Layer 6

where it's going to encapsulate the Layer 7 header

and data together, and then add its own Layer 6 header,

which contains its own metadata with information

about the presentation or encryption formats being used.

Next, it's going to pass this down to Layer 5

where it encapsulates the Layer 6 header

and the Layer 6 data

and it's going to add its own Layer 5 header

based on the metadata about the session.

As you can see, it's like taking a letter,

or in this case data, wrapping it in an envelope

and then writing some information on that envelope.

That's our header.

When we hand it to the next person,

they're going to put it in an envelope

and write their own metadata on the outside of the envelope

and then pass it to the next person.

And we keep doing this as we go down the layers

all the way down to Layer 1.

Now, the headers added at Layers 4, 3, 2, and 1

are very specific and they actually help ensure the message

is going to reach its final destination.

So let's take a look at the header that's added at Layer 4,

the transport layer.

Now, if you remember,

the transport layer uses different protocols

like TCP or UDP.

The TCP header has 10 mandatory fields,

totaling 20 bytes of information.

This includes our source port, the destination port,

the sequence number, the acknowledgement number,

the TCP data offset, the reserve data,

which is currently always going to be set to zero

because it's not really used,

the control flags, the window size, the TCP checksum,

the urgent pointer, and the mTCP optional data.

Now, you don't need to know all of these fields in depth,

but there are a couple that are pretty important.

For example, the source and destination ports

are pretty important to understand

because this helps determine

where the information is being sent from

and where it's being sent to,

and allows it to go through a firewall

by going to the right ports.

Also, the sequence number and acknowledgment numbers

are going to be used to ensure all the data

is properly received by the destination

when it's sent by the original transmitter.

So this is also important when you're using TCP.

Another important concept in the TCP header

is the control flags.

There are six control flags that are used

to manage data flow before, during,

and to stop the data communication when you're finished.

You should already be familiar with the three-way handshake.

That uses the SYN packet sent by the client,

the SYN-ACK packet that's sent by the server,

and the ACK packet that the client sends back to the server

at the end.

These packets are sent using the TCP flags of SYN or ACK

inside your TCP header.

Now, in addition to the SYN and ACK flags,

there's also four others: FIN, RST, PSH, and URG.

First, we have the SYN flag or synchronization flag.

This is by far the most well-known flag

in TCP communications because it's used to synchronize

the connection during the three-way handshake.

Next, we have the ACK or acknowledgement flag.

This is also used during the three-way handshake,

but in addition to that,

we use it to acknowledge the successful receipt

of all the packets during the communication.

The FIN or finished packet is used to tear down

the virtual connection created by the three-way handshake

and the SYN flag.

The FIN flag always appears when the last packets

are exchanged between a client and a server,

and the host is now ready to shut down that connection.

Next, we have the RST flag or reset flag.

This is going to be used when a client or server

receives a packet that it was not expecting

during the current connection.

For example, if you tried to establish a connection

with a server that didn't want to accept any new connections,

it could send back an RST or reset flag

to inform your client that it's not accepting connections

and automatically reject a request.

The next one we have is a PSH flag or push.

Now, a push flag is used to ensure

the data is given priority

and is processed at the sending or receiving ends.

Most often, this flag is added to a packet

at the beginning or end of a data transfer.

The final flag we have is URG or the urgent flag.

The urgent flag is like the push flag

and it identifies incoming data as urgent.

Now, the main difference here between push and urgent

is that push is used by the sender

to indicate data with a higher priority level.

Now, urgent, on the other hand,

is sent to tell the recipient to process it immediately

and ignore anything else that's in the queue.

With urgent, this could lead to packets

violating the first in first out priority order,

so it needs to be used

only by particular applications when necessary.

Now, if you're using UDP instead of TCP,

you're going to be using the User Datagram Protocol.

Now, when we look at the User Datagram Protocol header,

this is another transport layer or Layer 4 header

that's going to be used in our networks.

Remember, UDP is unreliable

and it's a connectionless protocol,

so its header is significantly smaller than TCP.

With UDP, we only have an eight byte header

instead of the 20 byte header used in TCP.

UDP only has four fields that are used:

the source port, the destination port, the length,

and the checksum.

The source and destination ports

are just like the ones used in TCP.

They dictate where the data is coming from

and where it's going to.

The length is used to indicate

how many bytes the total UDP packet is,

including the header and its data.

The checksum is not a mandatory field,

but instead it can be used to provide some validation

that the UDP data being sent was actually received

with some level of integrity.

Next, let's move down to Layer 3, the network layer.

As we move down another layer,

we're going to again encapsulate the data and add a header.

This time, we're going to add the IP

or internet protocol header.

The IP header is going to contain several fields,

including the IP version, the length of the IP header,

the type of service,

which was defined by the standard but never really used,

the total length of the packet and header,

the identifier, the flags, the fragmented offset,

the time to live, the protocol, the header checksum,

the source IP, the destination IP,

and the options and padding.

Now, as we continue down the layers,

we're going to reach Layer 2, the data link layer,

and this is going to encapsulate the data

by adding an Ethernet header.

Now, this header features just a few things,

including a destination MAC address, the source MAC address,

the EtherType field, and an optional VLAN tag

using either IEEE, 802.1q, or IEEE 802.1ad.

We're going to talk more about VLANs in a separate video though

because it's an important concept.

So let's talk about a MAC address.

A MAC address is a physical address that's used to identify

a network card on your local area network.

This allows our source to find our destination

by using this type of Layer 2 addressing.

This is what's processed by switches in your network.

Now, the EtherType field is used to indicate

which protocol is encapsulated in the payload event frame.

So if you're using IPv4 or IPv6,

this can be indicated here using the EtherType field.

Now, in addition to the Ethernet header,

a frame being sent at Layer 2 will also contain a payload.

In Ethernet, the minimum payload is 42 bytes

if VLANs are being used

and 46 bytes if no VLANs are being used.

Now, when you're trying to send a payload,

there is a maximum size to this,

known as an MTU or maximum transmission unit.

When we talk about payloads,

this is the data we're trying to send across the network.

By default, Ethernet uses an MTU of 1,500 bytes

as its maximum size.

Now, if you have a payload that's larger than 1,500 bytes,

then you need to allow for what's known as a jumbo frame.

This just means the frame is going to be larger

than 1,500 bytes.

To configure this on your switch,

you're going to reconfigure your MTU size

or your maximum transmission unit size

to larger than 1,500 bytes.

All right, that was a ton of information we just covered,

but let's review a couple of main concepts here.

First, remember, as data moves from Layer 7 to Layer 1,

we are going to encapsulate that data.

So as we move down the OSI layers,

we're going to encapsulate that data

and add a header at each of those layers.

At Layer 4, we're going to add our source

and destination ports.

At Layer 3, we add our source and destination IP addresses.

At Layer 2, we add our source and destination MAC addresses.

Now, once we get to Layer 1,

we're simply transmitting our Layer 2 frames

as a series of ones and zeros over the medium.

When it's received by the next device,

for example a switch,

it's going to put the frames back together

from the electrical, optical, or radio frequency signals

that it received over Layer 1.

Now, it's going to decapsulate the Layer 2 information

by reading the Ethernet header.

If the destination MAC is on one of the switch ports,

it's going to send the message to it.

If not, it's going to forward it to its default gateway,

which is a router.

This router then decapsulates the data to Layer 3,

and it reads the destination IP address.

If it's on its network,

it's going to forward the data to that device.

If not, it's going to re-encapsulate the data

and send it out its default gateway.

And then this process will continue

until the final destination or host is found.

Now, once that host is found,

it's going to keep decapsulating that information

all the way back up to Layer 7

where its application can read

and understand the underlying data.

Now, we're going to cover a lot more

about how this data transfer happens

when we talk about switches and routers

later in this course.

But for now, this is the basics you need to understand.

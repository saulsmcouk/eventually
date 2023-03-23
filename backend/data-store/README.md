# <p align="center"> SUPERCELL </p>

# <p align="center"> Building Contextual Empathy </p>

<img width="1087" alt="Screenshot 2022-03-22 at 14 04 23" src="https://user-images.githubusercontent.com/120366987/226589165-116c28ce-0d7e-4c97-a0a2-df2e67b40c2f.png">

## <p align="center"> Case Introduction: </p>

In an ideal situation, when a player is facing harmful, hurtful, dangerous, or problematic behaviour (we’ll call this collectively _disruptive_ going forward), either the person who is being targeted or someone who is witness to this behaviour will alert a moderator through some sort of reporting.

In reality, it’s not always that simple!

Sometimes a player is targeted in such a way that they feel threatened and isolated, other times they may not understand the insidious nature of the disruptive behaviour. In both cases, it’s unlikely that the behaviour will be reported, and therefore challenging to address.

This is a challenge in physical spaces as well, but in those physical spaces we have a few queues that we’ve developed in society to look out for. For example, on the playground we look for a vulnerable person who has been isolated in the corner of the field by the class bullies. In some societies, we’re careful to build lines of site to where we feel vulnerable people might be cornered, such as lonely alleys or under bridges.

In the digital space, we have plenty of signals, but trying to make sense of the signals is the challenge. We have things like tracked play-patterns, record of chat, certain types of behaviours (when they log in/off), who else is around, general sentiment of chat... and more. There are dozens of companies out there promising that AI can solve this, but we’re not there yet! In the meantime, we need to understand how to use the signals available in a user-friendly way to alert humans that something is going on.

To be clear, we have this mostly solved when it comes to using two players’ chat records when it comes to things like hateful, racist, or overtly sexual content. We’re looking to solve for the things that can’t be easily surfaced through chat alone.


## <p align="center"> Deep Dive: </p>

<p align="center"> Please visit us at our space for the deep dives and let's have a conversation. </p>


##  <p align="center"> Resources: </p>

## <p align="center"> Data </p>
You may or may not use the following partial datasets to help you come up with a solution to the challenge. The data consists of six zipped .csv files, containing chat message data, account level data, and data relevant to alliances (groups of players that play the game together).

The datasets are joinable by account_id and/or alliance_id.

As a part of your solution you may indicate what kind of additional data would be / have been helpful in reaching a better solution.

## chat_messages_1.csv and chat_messages_2.csv
Contains chat message data from users on 2023-03-01.

The message topic fields GENERAL_RISK, BULLYING, VIOLENCE, RELATIONSHIP_SEXUAL_CONTENT, VULGARITY, DRUGS_ALCOHOL, IN_APP,  ALARM, FRAUD, and HATE_SPEECH contain graded (from -1 to 7) by risk level, with -1 being that the topic is absent and 7 being high risk. All messages are also accompanied by an overall risk score (the field: risk). 

The field filtered_content contains an array of the filtered out words from the raw_message string.
The field is_family_friendly (0 or 1) informs whether this player is a chatting in an alliance environment that should be considered family friendly. That is the alliance contains young players that should be more protected from harm and sharing personal information.

Schema:

account_id:string

alliance_id:string

timestamp:timestamp

date:date

raw_message:string

filtered_message:string

filtered:integer

filtered_content:array[string]

risk:long

filter_detected_language:string

is_family_friendly:integer

GENERAL_RISK:long

BULLYING:long

VIOLENCE:long

RELATIONSHIP_SEXUAL_CONTENT:long

VULGARITY:long

DRUGS_ALCOHOL:long

IN_APP:long

ALARM:long

FRAUD:long

HATE_SPEECH:long


## accounts.csv
Contains additional account information for users that posted chat messages on 2023-03-01

The field active tells if the player was active on that day. Basically this should hold true for every account provided here.
The field level is the player level in the game. This can be thought of as an indicator of progression.

Schema:

account_id:string

alliance_id:string

session_count:long

session_duration:double

transaction_count:long

revenue:double

date:date

active:string

account_state:integer

last_active_date:date

level:integer

created_language:string

created_country_code:string

created_time:timestamp

session_count_today:long

session_duration_today:double

transaction_count_today:long

revenue_today:double

last_login_game_client_language:string

last_login_country_code:string


## alliance_ff.csv
Contains alliance family friendly (ff) status for alliances that contains user that posted chat messages on 2023-03-01

Family friendly means that the alliance contains young players that should be more protected from harm and sharing personal information.

Schema:

alliance_id:string

family_friendly:integer (-1 = no, 0 = unassigned, 1 = yes)

date:date

## alliance_membership.csv
Contains alliance membership information (actions of players joining, leaving, being kicked out, failed to join, etc) for alliances that contains user that posted chat messages on 2023-03-01

The field size indicates the amount of players in the alliance at the time of the given account alliance membership action taking place.
The field max_size indicates the maximum amount of players allowed in the alliance.

Schema:

account_id:string

alliance_id:string

timestamp:timestamp

date:date

action:string

size:integer

max_size:integer

## <p align="center"> Data sets </p>

[accounts.csv.zip](https://github.com/START-Hack/SUPERCELL_STARTHACK23/files/11016656/accounts.csv.zip)

[alliance_ff.csv.zip](https://github.com/START-Hack/SUPERCELL_STARTHACK23/files/11016658/alliance_ff.csv.zip)

[alliance_membership.csv.zip](https://github.com/START-Hack/SUPERCELL_STARTHACK23/files/11016662/alliance_membership.csv.zip)

[chat_messages_1.csv.zip](https://github.com/START-Hack/SUPERCELL_STARTHACK23/files/11016663/chat_messages_1.csv.zip)

[chat_messages_2.csv.zip](https://github.com/START-Hack/SUPERCELL_STARTHACK23/files/11016666/chat_messages_2.csv.zip)


## <p align="center"> Judging Criteria: </p>

### Impact
How relevant is the solution to the given problem? How will it change the way we think about the problem? How will the business, community, and people using the solution benefit?

### Innovation/creativity
How creative or innovative was the idea of the solution? Was the solution something that hasn’t been successfully implemented in the past (novelty)?  

### Policy
How well does the solution abide with different laws and regulations when in comes to user privacy and safety, especially in the case of young players. For example GDPR and COPPA compliance.

### Technical sophistication
How technically impressive is the solution? Does the solution utilise modern technologies and/or ML/AI in useful way?

### Feasibility/Robustness
Is the solution something that could be actually put into production with rather small efforts? Does it scale well when we are thinking about 100 million users per day and even more user based events per day? Will the cost/benefit ratio be balanced?



## <p align="center"> Point of Contact: </p>

<p align="center"> Nate, Albert and Lucas will be glad to answer your questions during the Deep Dive. We’ll also be available on Discord. </p>


## <p align="center"> Prize - the winning team members will each receive: </p>

### A Nintendo Switch and AirPods Pro

=== BusKirkConversation ===

= kirk_initiates
    ~ raise(water)
    -   Bus Driver:  I see you're new from around these parts. What makes you come all this way?
        Charlie crumpled the small note in their pocket at the question.
        *   Truthful [- I'm looking for someone.] 
            ~ raise(plant)
            This was the only lead they had. Maybe they knew something?
            Charlie: I'm looking for someone at Arbor Hollow.
            Bus Driver:  Oh, I stop here all the time, I know everyone in town!  Who're you looking for?
            Charlie: Um...

            **  Lost in Thought [- Just someone I haven't seen in a long time.]
                ~ raise(kirk_trust)
                Charlie: Just someone I haven't seen in a long time.
                Bus Driver: Well, that could be anybody!
                Charlie: But has anyone else been to the town recently?
                Bus Driver: Not in the last 5 years I'd say. 
                Bus Driver: There's only 20 locals these days, so it's a big deal when someone new decides to stay. 
                Bus Driver: They'll probably throw ya a welcomin' party! Maybe you'll find who you're lookin' for there.

            **  Half Truth [- Sorrel, She's offering me a place in her house.] 
                ~ lower(kirk_trust)
                Charlie: Sorrel, She's offering me a place in her house.
                Bus Driver: Ah Sorrel, the Town's Plant Guru! The only thing she cares about more than her plants is her little brother.
                Charlie: I think I'm working with her brother, actually.
                Bus Driver: He's a sweet kid, I'm sure y'all will get along. 
                Bus Driver: I reckon you're going to be working at the convenience store then? It's about time they got an extra pair of hands over there.

        *   Direct [- I got a job in town.]
            ~ raise(fire)
            Charlie: I got a job in town.
            Bus Driver: Oh really? Congrats! Where you workin' kid?

            **  Cooperative [- I landed a job at a convenience store.]
                ~ raise(kirk_trust)
                Charlie: I landed a job at a convenience store. Rise Your Spirits, I think? 
                Charlie: The owner seems really nice! He even went out of his way to find me housing.
                Bus Driver: Yeah, I love that place. I swear it has everything! 
                Bus Driver: And Pappy's one of a kind, so you're in good hands. He cares a lot about his employees and treats 'em like family.
                Charlie: That's good to hear, who else works there?
                Bus Driver: Just two other kids, Kunal and Bailey.  
                Bus Driver: (Bus Driver laughs) Those two are like night and day.
                Charlie:  I'm guessing they don't get along.
                Bus Driver:  Oh don't get me wrong, they're friends. They just don't always see eye to eye.

            **  Evasive [- They didn't tell me much.]
                ~ lower(kirk_trust)
                Charlie: They didn't tell me much.
                Bus Driver: Well there's really only two places hiring in town right now. 
                Bus Driver: There's the convenience store, Rise Your Spirits, and the restaurant, Sol Food. Everywhere else either filled or a one man job.      
                Charlie: Restaurant? Is the food any good?
                Bus Driver: The owner Su makes the best food I've ever tried. 
                Bus Driver: She's been runnin' that kitchen longer than I've been driving this route!
                Charlie: How long have you been on this route?
                Bus Driver: (Checks watch) Oh, about 40 minutes now. (she laughs)

        *   Evasive [- I'm just starting fresh.]
            Charlie looks out the window, distracted by the possiblilty of seeing their sister after so many years.
            This was the only lead they had, but not everyone had to know that.
            ~ raise(water)
            Charlie: I'm just starting fresh. Things are kinda... complicated back home.
            Bus Driver: Ah I know what you mean. A simple life in a small town can do the soul a lot of healing... 
            Bus Driver: Ya like hot springs kid? 

            **  Agreeable [- Um...]
                ~ raise(kirk_trust)
                Charlie: (sweats lightly) Um... I guess?
                Bus Driver: Good! There's a hot spring up in the mountains. There's also a handsome fella in town who runs the hot springs.
                The bus driver pauses, gauging for a response.
                Bus Driver: In any case, they got a lake too if you don't like your water hot. 
                Charlie: Uhh... Cool. Good to see all of my options are covered. 
                Bus Driver: Literally! (she laughs) I hope you find what you're looking for.

            **  Suspicious [- UHH...]
                ~ lower(kirk_trust)
                Charlie: (sweats profusely) UHH... Why??
                Bus Driver: There's a hot spring up in the mountains. Well, we got a lake too if you don't like your water hot. 
                Bus Driver: Actually, there's a pretty interesting story about that there lake!
                Charlie: Like an urban legend? Is there a monster living in it?
                Bus Driver: Beats me. It's said to be a place where lost souls go to reflect. 
                Bus Driver: There's a girl that spends too much time staring into that glorified puddle. I'm sure she can tell you all about it when you get into town. 

    - Regardless, I think you'll have fun. 'Tis a quaint little town.

    -> LeavingTheBus

// = charlie_initiates
//     ~ raise(plant)
//     ~ raise(fire)
//     -   Charlie: So…  Do many people visit this town?
//         Bus Driver: Not that many people stay here, but there's a lot of travelers passing through.
//         Charlie:
//         Choice 1 (water):  
//         Charlie: 
//         Bus Driver: 
//         Choice 2 (plant):
//         Charlie:  What are the people in this town like?
//         Bus Driver: They're like any regular folk, albeit with their own quirks. 
//         Choice 3 (fire):
//         Charlie:  ...This place is pretty far out in the middle of the woods, any bigfoot sightings?
//         Bus Driver: I don't know about Bigfoot, but there's a legend about the fog here. 
//         Charlie looks out the window at the rolling fog. 
//         Charlie: (Internal) I think I liked Bigfoot better. 
//     -> LeavingTheBus

= LeavingTheBus
-> END


---
id: vw10cdpd016wcpwotok00mo
title: Gmail Alias Bad for Delivery
desc: ''
updated: 1707234198204
created: 1707182350927
topic: etc
---

Turns out sending email with gmail alias affects email deliverability - this is after having the whole DMARK, DKMI, SPF alphabet soup configured 🤦‍♂️

<image alt="bad email" src="https://ik.imagekit.io/fpjzhqpv1/Cursor_edU56VG7O.png?updatedAt=1707183135223" height="600px"/>

Did some digging (aka search google with `+ reddit`) and found this [post](https://www.reddit.com/r/gsuite/comments/rxj3ec/gsuite_alias_domain_emails_going_directly_to/) with the following comment:

    Yeah, that’s how it works for sending using an alias or “on behalf of”… it will just never smell as clean as the primary domain to receiving emails servers.
    That’s the “big” 0.249 hit on your score

Fortunately, the fix was simple. Remove the alias and add another user in gsuite. This fixed the deliverability problem and means we have the privilege of paying @Google  more money 🙄

<image alt="good email" src="https://ik.imagekit.io/fpjzhqpv1/Cursor_and_Newsletters_spam_test_rIBZJyfMy.png?updatedAt=1707183216008" height="600px"/>


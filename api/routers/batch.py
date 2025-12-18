from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timezone
from faker import Faker
import random

router = APIRouter()

fake = Faker()
Faker.seed(42)

AIRLINES = ['Virgin America', 'United', 'Southwest', 'Delta', 'US Airways', 'American']
SENTIMENTS = ['neutral', 'positive', 'negative']
NEGATIVE_REASONS = [
    None,
    'Bad Flight',
    "Can't Tell",
    'Late Flight',
    'Customer Service Issue',
    'Flight Booking Problems',
    'Lost Luggage',
    'Flight Attendant Complaints',
    'Cancelled Flight',
    'Damaged Luggage',
    'longlines'
]

class Tweet(BaseModel):
    airline_sentiment_confidence: float
    airline: str
    negativereason: Optional[str]
    tweet_created: str 
    text: str

def generate_tweet() -> Tweet:
    airline = random.choice(AIRLINES)
    sentiment = random.choices(
        SENTIMENTS,
        weights=[0.3, 0.25, 0.45],
        k=1
    )[0]

    confidence = round(random.uniform(0.5, 1.0), 3) 
    if sentiment == 'neutral':
        confidence = round(random.uniform(0.3, 0.7), 3)

    negativereason = None
    if sentiment == 'negative':
        negativereason = random.choice(NEGATIVE_REASONS[1:]) 
    elif sentiment == 'neutral':
        negativereason = random.choice(NEGATIVE_REASONS) 

   
    handles = {
        'Virgin America': '@VirginAmerica',
        'United': '@united',
        'Southwest': '@SouthwestAir',
        'Delta': '@Delta',
        'US Airways': '@USAirways',
        'American': '@AmericanAir'
    }
    handle = handles[airline]

    if sentiment == 'positive':
        texts = [
            f"{handle} Great service today — flight was on time and crew was amazing! ✈️👏",
            f"Shoutout to {handle} for upgrading me last minute. You made my day!",
            f"Smooth flight with {handle} — love the new seats and in-flight snacks. 🍪",
            f"{handle} Great experience today! Crew was friendly and flight was smooth.",
            f"Shoutout to {handle} for the amazing service. Made my trip stress-free!",
            f"Loved flying with {handle} — comfortable seats and tasty snacks. 🍫",
            f"{handle} Excellent on-time service and super helpful staff.",
            f"Big thanks to {handle} for making my flight so enjoyable! 🥳",
            f"{handle} Smooth boarding, friendly crew, and comfy ride. Highly recommend! 👍",
            f"Flying with {handle} was fantastic! The in-flight entertainment was top-notch. 🎬",
            f"{handle} Thank you for the upgrade — truly made my day! ✨",
            f"Wonderful flight experience with {handle}. Everything was perfect!",
            f"{handle} Staff was courteous and helpful, and boarding was super fast. 👏",
            f"Impressed with {handle} today — great service and very punctual. 🌟",
            f"{handle} Loved the new seating and snacks on board. Thanks for a great flight! 🍪",
            f"Flying with {handle} is always a pleasure — smooth ride and friendly staff.",
            f"{handle} Exceptional service today. Crew went above and beyond!",
            f"Thank you {handle} for an amazing journey — comfy seats and great service. 🥰",
            f"{handle} Quick boarding, smooth takeoff, and attentive crew. Perfect flight!",
            f"Had a wonderful flight with {handle}. Everything ran smoothly and crew was amazing. 😊",
            f"{handle} Great service all the way — would fly again in a heartbeat! ❤️",
            f"Shoutout to {handle} for making travel so easy and pleasant.",
            f"{handle} Loved the attention to detail and friendly staff on board.",
            f"Flying with {handle} is always stress-free and enjoyable. Highly recommend! 🌟",
            f"{handle} Excellent experience today — on-time and comfortable!",
            f"Thanks {handle} for the great service and smooth flight. Made my trip so easy! ✈️",
            f"{handle} Crew was attentive, boarding was seamless, and flight was enjoyable.",
            f"Big thanks to {handle} — in-flight snacks were delicious and staff was amazing! 🍫",
            f"{handle} Loved the upgrade and friendly service today. Truly appreciated! ✨",
            f"Flying with {handle} always makes me smile — smooth ride and comfy seats.",
            f"{handle} Excellent flight experience — professional crew and on-time arrival. 🌟",
            f"Thanks {handle} for making my journey pleasant and hassle-free! 👏",
            f"{handle} Great flight, wonderful staff, and excellent amenities on board! 🥳",
        ]
    elif sentiment == 'negative':
        texts = [
            f"{handle} why are your first fares in May over three times more than other carriers when all seats are available to select???",
            f"{handle} flight delayed 4 hours with no updates. Terrible communication. #disappointed",
            f"{handle} lost my luggage AGAIN. This is the third time this year. Unacceptable.",
            f"{handle} customer service hung up on me. What kind of support is that?!",
            f"{handle} 2-hour line at check-in for pre-paid bags. Ridiculous inefficiency.",
            f"{handle} Flight was delayed again with zero updates. Completely unacceptable. #frustrated",
            f"{handle} Why is the boarding process always chaotic? Total lack of organization.",
            f"{handle} Lost my luggage for the second time this month. Seriously disappointing.",
            f"{handle} Customer support keeps transferring me with no resolution. Very poor service.",
            f"{handle} Seats were broken and uncomfortable — not what I paid for. #disappointed",
            f"{handle} 3-hour delay and no compensation offered. Very frustrating experience.",
            f"{handle} Why are your fares suddenly double compared to competitors? Unfair pricing!",
            f"{handle} Flight cancelled last minute and no clear alternative offered. #annoyed",
            f"{handle} Staff was rude and unhelpful during check-in. Totally unacceptable!",
            f"{handle} Overbooked flight and they asked volunteers last minute. Very frustrating.",
            f"{handle} My luggage arrived damaged and no apology was given. #badservice",
            f"{handle} Boarding process was messy and disorganized. Not impressed. 👎",
            f"{handle} Lost my baggage again. This is getting ridiculous! #fail",
            f"{handle} Long security lines with no staff assistance. Extremely inefficient.",
            f"{handle} Customer support ignored my emails for days. Very poor experience.",
            f"{handle} Why are your flights always delayed without explanation? #frustrated",
            f"{handle} Seats were dirty and food was terrible. Not flying with you again.",
            f"{handle} Charged extra fees for everything. Total money grab. #disappointed",
            f"{handle} No updates for delayed flight. Left waiting for hours. Unacceptable.",
            f"{handle} Staff was unprofessional and unhelpful. Worst airline experience ever.",
            f"{handle} Overbooked my seat and offered nothing in compensation. Ridiculous!",
            f"{handle} Lost luggage and no one answers the phone. Frustrating! #badservice",
            f"{handle} Flight delayed multiple times with zero communication. Terrible.",
            f"{handle} Paid for extra baggage and still had to wait in long lines. Unfair!",
            f"{handle} My booking was messed up and customer support couldn’t fix it. #fail",
            f"{handle} Boarding was chaotic and stressful. Very poorly managed. 👎",
            f"{handle} Flight attendants were rude and ignored passengers. Unacceptable.",
            f"{handle} Lost luggage AGAIN. How is this still happening?! #disappointed",
            f"{handle} Charged hidden fees with no prior notice. Total scam. #annoyed",
            f"{handle} Delayed departure with no explanation. Very poor communication.",
        ]
    else: 
        texts = [
            f"{handle} flight was fine. Boarding took a while, but nothing major.",
            f"Average experience with {handle}. On time, but seat was a bit tight.",
            f"Checked in online with {handle}, flight happened. No complaints, no praise.",
            f"{handle} Flight went as expected. Nothing extraordinary, but no issues either.",
            f"Average flight with {handle}. On time, boarding was okay, seats standard.",
            f"{handle} Checked in, boarded, and flew. Standard experience, nothing special.",
            f"{handle} Flight was on schedule. Cabin was fine, no problems to report.",
            f"{handle} Nothing notable about this flight. It went as planned.",
            f"{handle} Standard service from {handle}. Seats, snacks, and crew were average.",
            f"{handle} Flight was neither good nor bad. Just a regular trip.",
            f"{handle} Boarding took a bit, but flight was smooth. Neutral experience.",
            f"{handle} Checked in fine, flight departed on time. Nothing more to add.",
            f"{handle} Seats were okay, flight was on time. Typical experience.",
            f"{handle} Flight went without issues, but nothing stood out. Neutral.",
            f"{handle} Standard airline experience. On time and routine service.",
            f"{handle} Flight happened as scheduled. Crew was adequate, nothing extra.",
            f"{handle} Average experience with {handle}. Everything as expected.",
            f"{handle} Boarding and flight were okay. No complaints or highlights.",
            f"{handle} Flight was fine. Minor delays, but nothing noteworthy.",
            f"{handle} Routine flight with {handle}. On time and uneventful.",
            f"{handle} Checked in, boarded, and arrived on time. Neutral overall.",
            f"{handle} Nothing remarkable about the flight. Standard procedure.",
            f"{handle} Flight was okay. No major issues or exceptional service.",
            f"{handle} Average trip with {handle}. Standard seats and service.",
            f"{handle} Flight occurred as expected. Boarding was normal, crew fine.",
            f"{handle} No issues during flight. Typical airline experience.",
            f"{handle} Flight was fine. Took off on time and arrived as scheduled.",
            f"{handle} Standard boarding, standard flight. Neutral experience.",
            f"{handle} Routine travel with {handle}. Everything went smoothly.",
            f"{handle} Flight was ordinary. Crew and service as expected.",
            f"{handle} On-time flight with no special issues. Neutral overall.",
            f"{handle} Checked in, boarded, and flew normally. Nothing special.",
            f"{handle} Flight went okay. Seats and service were standard, nothing more.",
            f"{handle} Routine airline experience. On time, no complaints, no praise.",
        ]

    text = random.choice(texts)
    
    if random.random() < 0.3:
        text += " " + fake.sentence(nb_words=6).rstrip(".")

    tweet_created = datetime.now(timezone.utc).isoformat()

    return Tweet(
        airline_sentiment_confidence=confidence,
        airline=airline,
        negativereason=negativereason,
        tweet_created=tweet_created,
        text=text
    )

@router.get("/batch", response_model=List[Tweet])
def get_microbatch(batch_size: int = 10):
    
    if not (1 <= batch_size <= 100):
        batch_size = min(max(batch_size, 1), 100)  

    return [generate_tweet() for _ in range(batch_size)]


import requests
import random

SUGGESTIONS_TOTAL = 100
SUGGESTION_IDS = range(1, SUGGESTIONS_TOTAL + 1)

##We need the API site below where it says 'api site url'
def get_suggestion(suggestion_id):
    return requests.get(f"api site url{suggestion_id}")

def get_random_suggestion_list(love_language_id):
    if love_language_id == "words_of_affirmation":
        suggestion_list = words_of_affirmation
    elif love_language_id == physical_touch:
        suggestion_list = physical_touch
#do this for all of the love languages
    random_suggestion_id = random.sample(SUGGESTION_IDS, k=1)
    suggestions =
    ## put in here, grab an item from the list - an index number in the list
    ##return [get_suggestion(suggestion_id) for suggestion_id in random_suggestion_id]
    return(suggestion)

def words_of_affirmation():
    words_of_affirmation = [
        "Say something nice to your partner! visit:https://www.verywellmind.com/words-of-affirmation-4783539 for more detail.",
        "Tell them how much you care! visit:https://liveboldandbloom.com/02/relationships/affirmation-love-language for more detail.",
        "Say the right thing, tell your partner you love them! visit:https://www.lovepanky.com/love-couch/better-love/words-of-affirmation for more detail.",
        "Tell your partner you love them! visit:https://pairedlife.com/relationships/Words-of-Affirmations-Examples-Love-Language for more detail.",
        "Tell your partner how much you care about them, why not try writing it down? visit:https://www.moonpig.com/uk/ for more detail.",
        "Complement on their outfit!",
        "Complement on their new hair!",
        "Reassure your love for them!",
        "Validate their feelings!",
        "Tell them how proud you are of your partner!"]
    ##words_of_affirmation_copy = words_of_affirmation.copy()
    ##suggestion = random.choice(words_of_affirmation_copy)
    return(words_of_affirmation)
    ##words_of_affirmation_copy.remove(suggestion)

def physical_touch():
    physical_touch = [
        "Could your partner enjoy a massage? visit:https://www.wikihow.com/Massage-Your-Partner for more detail."
        "Hug it out with your partner. visit:https://www.healthline.com/health/hugging-benefits for more detail."
        "Time to switch up your positions. visit:https://www.amazon.co.uk/Kama-Sutra-Position-Day-New/dp/024150645X/ref=sr_1_1?crid=J7RZ7MRM10Q9&keywords=kama+sutra&qid=1659803296&sprefix=calma+su%2Caps%2C65&sr=8-1 for more detail."
        "Why not plan a romantic treasure hunt for your partner? visit:https://www.wikihow.com/Plan-a-Romantic-Treasure-Hunt for more detail."
        "Greet your partner with a nice cheek kiss!"
        "Try some new sex positions! visit:https://www.cosmopolitan.com/sex-love/a38400662/these-items-belong-on-your-2022-sex-bucket-list/ for more detail."
        "Hold your partner's hand! visit: for more detail."
        "Brush your partner's hair! visit:https://www.boots.com/beauty/hair/brushes-and-combs for more detail."
        "Read your partner's palm! visit:https://www.cosmopolitan.com/lifestyle/a29623751/how-to-read-palms-beginners/ for more detail."
        "Caresses"
    ]
    physical_touch_copy = physical_touch.copy()
    suggestion = random.choice(physical_touch_copy)
    print(suggestion)
    physical_touch_copy.remove(suggestion)

def quality_time():
    quality_time = [
        "It's time for a holiday! Check out booking.com. visit:https://www.booking.com/ for more detail.",
        "Find a spa day on groupon! visit:https://www.groupon.co.uk/ for more detail.",
        "Try minigolf! visit:https://www.redbull.com/gb-en/uk-coolest-crazy-golf-mini-golf-courses for more detail.",
        "It's time to go abroad with your partner! visit:https://www.skyscanner.net/ for more detail.",
        "It's time to be a better listener. visit:https://psychcentral.com/relationships/listen-better-in-relationships for more detail.",
        "Thought about a trip to the cinema? Could be just what you need. visit:https://www.myvue.com/ for more detail.",
        "Walk it out! Here's a link to the UK's best walks. visit:https://www.nationaltrust.org.uk/features/celebrating-britains-100-favourite-walks for more detail.",
        "Here's a link to the UK's top airbnbs. visit:https://www.timeout.com/uk/travel/best-airbnbs-in-uk for more detail.",
        "Here's opentable's most romantic restaurants in the UK list. Take your pick! visit:https://www.opentable.co.uk/lists/most-romantic-restaurants-uk-2020 for more detail.",
        "Maybe it's time to re-up that subscription to Netflix and chill? visit:https://www.netflix.com/gb/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse for more detail."
    ]
    quality_time_copy = quality_time.copy()
    suggestion = random.choice(quality_time_copy)
    print(suggestion)
    quality_time_copy.remove(suggestion)

def acts_of_service():
    acts_of_service = [
        "Make your partner breakfast! Here's a link:https://www.bbc.co.uk/food/recipes/fluffyamericanpancak_74828 to a recipe and place to order:https://www.ocado.com/webshop/startWebshop.do the ingredients.",
        "Get your partner's house professionally cleaned! Here's a link to purchase a house-cleaning voucher. visit: for more detail.",
        "Get your partner's car cleaned! Here's a link to a car-wash voucher. visit:https://www.americancarwash.co.uk/offers/ for more detail.",
        "Help your partner's financial situation! Here's a link to an investment platform. visit:https://www.vanguardinvestor.co.uk/ for more detail.",
        "Want to make an event even more memorable? Find some photographer on Fiverr near your area! visit:https://www.fiverr.com/categories/video-animation/local-photographers for more detail.",
        "If you notice your partner needs some household fixing, that means you are very observant. Maybe finding a plumber would help demonstrating that to them! visit:https://my-plumber.co.uk/ for more detail.",
        "Say Thank you to your partner to acknowledge their love and car for you! visit:https://www.moonpig.com/uk/ for more detail.",
        "Make reservation for date nights! visit:https://trulyexperiences.com/uk/ for more detail.",
        "Cook your partner dinner! visit:https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjukJWQ8bL5AhWaiNUKHVUMBhEYABABGgJ3cw&ohost=www.google.com&cid=CAESa-D2R0JJT0G5_Ja4llzp8QOkQZPWwtvMh-5R3nirXaJ-T9o51BmcytcyQjhsWk5vB6IHEXbvVIWsBpOeaeqERh2-3yeFVf-BDTznsPMQ1-LkcMFkSe_AkLG_MC-zUwN82sJd4elbanjm1YND&sig=AOD64_1fq4ldAWlHXaWTU9s9851lKY2Z-Q&q&adurl&ved=2ahUKEwi9-ouQ8bL5AhWPhFwKHUS7DWYQ0Qx6BAgFEAM for more detail.",
        "Ask "What can I do to help?""
    ]
    acts_of_service_copy = acts_of_service.copy()
    suggestion = random.choice(acts_of_service_copy)
    print(suggestion)
    acts_of_service_copy.remove(suggestion)

def gift_giving():
    gift_giving = [
        "Get your partner to make an Amazon wishlist! visit:https://www.amazon.co.uk/hz/wishlist/intro for more detail.",
        "Has your partner got a vinted or depop account? Purchase something they have liked! visit:https://www.vinted.co.uk/ and https://www.depop.com/ for more detail.",
        "Give the gift of caffeine! visit:https://www.pret.co.uk/en-GB/pretcoffeesub for more detail.",
        "Tiktok viral gadgets might just be your lifesaver! visit:https://www.housebeautiful.com/shopping/g38584965/viral-tik-tok-gadgets/ for more detail.",
        "Get your partner the latest fashion from ASOS. visit:https://www.asos.com/ for more detail.",
        "Get your partner the best gift at the best price from Groupon. visit:https://www.groupon.co.uk/gift-ideas for more detail.",
        "Get your partner the cutest personalised gift from Etsy. visit:https://www.etsy.com/uk/market/gifts?utm_source=google&utm_medium=cpc&utm_term=etsy%20gifts_e&utm_campaign=Search_UK_Brand_GGL_ENG_Gifting_General_All&utm_ag=Gifts&utm_custom1=_k_Cj0KCQjworiXBhDJARIsAMuzAuwr831J0wabEAzrtX1KOPjQQFYu6i8sJpopRA29fTBYFGkHp8olOFwaAmR_EALw_wcB_k_&utm_content=go_10576744742_104265966933_542766752040_aud-1023599305603:kwd-20158709728_c_&utm_custom2=10576744742&gclid=Cj0KCQjworiXBhDJARIsAMuzAuwr831J0wabEAzrtX1KOPjQQFYu6i8sJpopRA29fTBYFGkHp8olOFwaAmR_EALw_wcB for more detail.",
        "Get your partner the perfect gift from Buyagift! visit:https://www.buyagift.co.uk/ for more detail.",
        "Plan a surprise holiday for your partner! visit:https://www.loveholidays.com/sem/package.html?WT.mc_id=pgo-35492159457-kwd-132616509&ch=gen&gclid=Cj0KCQjworiXBhDJARIsAMuzAuztgTCP4DlFSNs51xznQnRIb8jjpZSjPl7D2pCEqqGZLm8mQE8WTicaAp66EALw_wcB for more detail.",
        "Get your partner a special jewelery! visit:https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjl8Pna8bL5AhXGstUKHYwoB7QYABAoGgJ3cw&ohost=www.google.com&cid=CAESa-D2y-IgVO8_MKAPnMkYCltC-y43w86CzPrmAmovRDKG-DnXAZGSBK9XwD72INQy0TmDRhZfmJIxIu478GkxM6jhAcJTcxL_xHgzYgt0BmwjlpfqUHxM6kyCuIKHG8_QwdFaNkeFpJ5di0ft&sig=AOD64_3pMsY5ssX9oBVlW9oj99UX1pO6wQ&q&adurl&ved=2ahUKEwj-leva8bL5AhW1Q0EAHU6xCy8Q0Qx6BAgFEAE for more detail."
    ]
    gift_giving_copy = gift_giving.copy()
    suggestion = random.choice(gift_giving_copy)
    print(suggestion)
    gift_giving_copy.remove(suggestion)

def love_language_randomizer():
    love_language = input("Which love language would you like to try?\n1.Words of Affirmation\n2.Physical Touch\n3.Quality Time\n4.Acts of service\n5.Gift-giving ".lower())
    while True:
        if love_language == "words of affirmation":
            words_of_affirmation()
        if love_language == "physical touch":
            physical_touch()
        if love_language == "quality time":
            quality_time()
        if love_language == "acts of service":
            acts_of_service()
        if love_language == "gift giving":
            gift_giving()
        again = input("Would you like another suggestion? yes/no ".lower())
        if again == "yes":
            continue
        else:
            another = input("Would you like to try another love language? yes/no ".lower())
            if another == "yes":
                love_language_randomizer()
            else:
                print("Thank you for not giving up on love!")
                break
        break
love_language_randomizer()

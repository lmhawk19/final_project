CREATE DATABASE diy_couples_therapy;
USE diy_couples_therapy;

CREATE TABLE love_languages (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

CREATE TABLE suggestions (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    love_language_id INTEGER NOT NULL,
    content VARCHAR(255) NOT NULL,
    url VARCHAR(255),
    suggester VARCHAR(50) NOT NULL DEFAULT 'DIY Couples Therapy',
    starred BOOLEAN NOT NULL DEFAULT FALSE,

    FOREIGN KEY (love_language_id) REFERENCES love_languages (id)
);

INSERT INTO love_languages
(id, name, description)
VALUES
(1, 'Words of affirmation', 'Words of affirmation are words that effectively communicate your love, appreciation, and respect for your partner. People with words of affirmation as their love language value verbal acknowledgements of affection, compliments, words of appreciation, and verbal encouragement.'),
(2, 'Quality time', 'Having quality time as your love language means that you value when your partner actively wants to spend time with you and is always keen to hang out. Active listening, eye contact, and full presence are particularly prioritized for those who have quality time as their love language.'),
(3, 'Acts of service', 'Acts of service focus on specific actions that show you care and understand your partner. If your partner is a firm believer in “Actions speak louder than words”, this may be their love language. Cooking a meal or doing laundry are all acts of service as they require thought, time, and effort.'),
(4, 'Receiving gifts', 'Receiving gifts isn’t necessarily all about the material things - it just means that a meaningful or thoughtful gift makes you feel loved and appreciated. The careful reflection, the deliberate choice of the object, and the emotional benefits from receiving the gift mean the world.'),
(5, 'Physical touch', 'Physical touch is all about physical signs of affection, including kissing, holding hands, cuddling on the couch, and sex. People with physical touch as their love language feel most content, warm, comfortable and connected in their relationship through physical intimacy.');

INSERT INTO suggestions
(love_language_id, content, url, starred)
VALUES
(1, 'Say something nice to your partner', 'https://www.verywellmind.com/words-of-affirmation-4783539', TRUE),
(1, 'Tell your partner how much you care', 'https://liveboldandbloom.com/02/relationships/affirmation-love-language', TRUE),
(1, 'Tell your partner you love them', 'https://www.lovepanky.com/love-couch/better-love/words-of-affirmation', TRUE),
(1, 'Write a note to your partner saying how much you care about them', 'https://www.moonpig.com/uk/', TRUE),
(1, 'Complement your partner on their outfit', NULL, TRUE),
(1, 'Complement your partner on their new hair', NULL, TRUE),
(1, 'Reassure your partner of your love for them', NULL, TRUE),
(1, 'Validate your partner\'s feelings', NULL, TRUE),
(1, 'Tell your partner how proud you are of them', NULL, TRUE),
(2, 'Take your partner on a holiday', 'https://www.booking.com/', TRUE),
(2, 'Find a spa day on groupon', 'https://www.groupon.co.uk/', TRUE),
(2, 'Go minigolfing with your partner', 'https://www.redbull.com/gb-en/uk-coolest-crazy-golf-mini-golf-courses', TRUE),
(2, 'Visit another country with your partner', 'https://www.skyscanner.net/', TRUE),
(2, 'Practise active listening', 'https://psychcentral.com/relationships/listen-better-in-relationships', TRUE),
(2, 'Go to the cinema with your partner', 'https://www.myvue.com/', TRUE),
(2, 'Go on a walk with your partner', 'https://www.nationaltrust.org.uk/features/celebrating-britains-100-favourite-walks', TRUE),
(2, 'Stay in one of the UK\'s top AirBnBs with your partner', 'https://www.timeout.com/uk/travel/best-airbnbs-in-uk', TRUE),
(2, 'Visit a romantic restaurant with your partner', 'https://www.opentable.co.uk/lists/most-romantic-restaurants-uk-2020', TRUE),
(2, 'Maybe it\'s time to re-up that subscription to Netflix and chill?', 'https://www.netflix.com/gb/', TRUE),
(3, 'Make your partner breakfast', 'https://www.bbc.co.uk/food/recipes/fluffyamericanpancak_74828', TRUE),
(3, 'Get your partner\'s house professionally cleaned', NULL, TRUE),
(3, 'Get your partner\'s car cleaned', 'https://www.americancarwash.co.uk/offers/', TRUE),
(3, 'Help your partner with their financial situation', 'https://www.vanguardinvestor.co.uk/', TRUE),
(3, 'Want to make an event even more memorable? Find a local photographer', 'https://www.fiverr.com/categories/video-animation/local-photographers', TRUE),
(3, 'Find a plumber if you notice your partner needs something in their house fixing', 'https://my-plumber.co.uk/', TRUE),
(3, 'Make a reservation for date night', 'https://trulyexperiences.com/uk/', TRUE),
(3, 'Cook dinner for your partner', NULL, TRUE),
(3, 'Ask your partner what you can do to help', NULL, TRUE),
(4, 'Get your partner to make an Amazon wishlist', 'https://www.amazon.co.uk/hz/wishlist/intro', TRUE),
(4, 'Has your partner got a Vinted account? Purchase something they\'ve liked', 'https://www.vinted.co.uk/', TRUE),
(4, 'Has your partner got a Depop account? Purchase something they\'ve liked', 'https://www.depop.com/', TRUE),
(4, 'Give the gift of caffeine', 'https://www.pret.co.uk/en-GB/pretcoffeesub', TRUE),
(4, 'Tiktok viral gadgets might just be your lifesaver', 'https://www.housebeautiful.com/shopping/g38584965/viral-tik-tok-gadgets/', TRUE),
(4, 'Get your partner the latest fashion from ASOS', 'https://www.asos.com/', TRUE),
(4, 'Get your partner the best gift at the best price from Groupon', 'https://www.groupon.co.uk/gift-ideas', TRUE),
(4, 'Get your partner the cutest personalised gift from Etsy', 'https://www.etsy.com/uk/market/gifts', TRUE),
(4, 'Get your partner the perfect gift from Buyagift', 'https://www.buyagift.co.uk/', TRUE),
(4, 'Plan a surprise holiday for your partner', 'https://www.loveholidays.com/sem/package.html', TRUE),
(4, 'Get your partner some special jewellery', NULL, TRUE),
(5, 'Give your partner a massage', 'https://www.wikihow.com/Massage-Your-Partner', TRUE),
(5, 'Hug it out with your partner', 'https://www.healthline.com/health/hugging-benefits', TRUE),
(5, 'Plan a romantic treasure hunt for your partner', 'https://www.wikihow.com/Plan-a-Romantic-Treasure-Hunt', TRUE),
(5, 'Greet your partner with a nice cheek kiss', NULL, TRUE),
(5, 'Try some new positions', 'https://www.cosmopolitan.com/sex-love/a38400662/these-items-belong-on-your-2022-sex-bucket-list/', TRUE),
(5, 'Hold your partner\'s hand', NULL, TRUE),
(5, 'Brush your partner\'s hair', 'https://www.boots.com/beauty/hair/brushes-and-combs', TRUE),
(5, 'Read your partner\'s palm', 'https://www.cosmopolitan.com/lifestyle/a29623751/how-to-read-palms-beginners/', TRUE),
(5, 'Give your partner some caresses', NULL, TRUE);

INSERT INTO suggestions
(love_language_id, content, url, suggester)
VALUES
(1, 'When your partner is complaining about their day, don\'t offer solutions, just validate their feelings', NULL, 'Lucy'),
(1, 'Be unequivocally on your partner\'s side. If your partner is annoyed with someone or something, verbally agree', NULL, 'Luke'),
(1, 'Create a words jar filled with words to describe your partner', 'https://www.papier.com/stationery/', 'Reema'),
(2, 'Take a day off of social media and screens. Use the day to really talk to and spend quality time with your partner', NULL, 'Elsa'),
(2, 'Housesit for someone for a change of scenery and a cheaper holiday alternative', NULL, 'Anya'),
(2, 'Join Classpass and do an exercise class with your partner', 'https://classpass.com/plans', 'John'),
(2, 'Get some delicious food and picnic supplies for a picnic', 'https://www.tesco.com/', 'Phoebe'),
(2, 'Bake with your partner', 'https://faircake.co.uk/online-school/', 'Craig'),
(2, 'Listen to a podcast with your partner', 'https://www.bbc.co.uk/sounds/podcasts', 'Oliver'),
(2, 'Make some art with your partner for your living room', 'https://www.dulux.co.uk/en', 'Reema'),
(3, 'Suggest that you visit your partner\'s family or friends they don\'t always get to see', NULL, 'Eric'),
(3, 'Hire a freelancer to complete a task your partner needs or wants doing', 'https://www.fiverr.com/', 'Holly'),
(3, 'Get your partner a Headspace subscription to improve their mental health', 'https://www.headspace.com/', 'Ben'),
(3, 'Make your partner a packed lunch for work', NULL, 'Thomas'),
(4, 'Pay attention to your partner\'s home and notice if anything is broken or damaged. Buy that item', NULL, 'Christina'),
(4, 'Send your partner flowers', 'https://www.bloomandwild.com/', 'Thor'),
(4, 'Try a gift hamper', 'https://www.hampers.com/gift-range', 'Magnus'),
(4, 'Treat your partner to an activity trip such as the spa, shooting at a range, or a helicopter ride', NULL, 'Joy'),
(4, 'Make your partner a gift such as a painting or a piece of pottery', NULL, 'James'),
(5, 'Get closer physically with a salsa or partners dance class', NULL, 'James'),
(5, 'Put your arm around your partner or hold their hand while you\'re out in public', NULL, 'Luna'),
(5, 'Rub your partners feet for them after a long day at work', NULL, 'Henry');

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User


engine = create_engine('sqlite:///itemCatalog.db')
Base.metadata.bind = engine
# bind code and engine
DBSession = sessionmaker(bind= engine)
#create instance of DBSession()
session = DBSession()

#add category entries and stage them
actionCategory = Category(title = 'Action')
session.add(actionCategory)
comedyCategory = Category(title = 'Comedy')
session.add(comedyCategory)
dramaCategory = Category(title = 'Drama')
session.add(dramaCategory)
fantasyCategory = Category(title = 'Fantasy')
session.add(fantasyCategory)
horrorCategory = Category(title = 'Horror')
session.add(horrorCategory)
thrillerCategory = Category(title = 'Thriller')
session.add(thrillerCategory)
session.commit()

#add action items
session.add(Item(title = 'Inception', description = 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', category_relationship = actionCategory))
session.add(Item(title = 'Gladiator', description = 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.', category_relationship = actionCategory))
session.add(Item(title = 'The Revenant', description = 'A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.', category_relationship = actionCategory))
session.add(Item(title = ' James Bond 007 - Casino Royale', description = 'Armed with a license to kill, Secret Agent James Bond sets out on his first mission as 007, and must defeat a private banker to terrorists in a high stakes game of poker at Casino Royale, Montenegro, but things are not what they seem.', category_relationship = actionCategory))
session.commit()

#add comedy items
session.add(Item(title = 'Kingsman: The Secret Service', description = 'A spy organization recruits an unrefined, but promising street kid into the agencys ultra-competitive training program, just as a global threat emerges from a twisted tech genius.', category_relationship = comedyCategory))
session.add(Item(title = 'White Chicks', description = 'Two disgraced FBI agents go way undercover in an effort to protect hotel heiresses the Wilson Sisters from a kidnapping plot.', category_relationship = comedyCategory))
session.add(Item(title = 'Hangover', description = 'Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.', category_relationship = comedyCategory))
session.add(Item(title = 'Kill the Boss', description = 'Three friends conspire to murder their awful bosses when they realize they are standing in the way of their happiness.', category_relationship = comedyCategory))
session.commit()

#add drama items
session.add(Item(title = 'Interstellar', description = 'A team of explorers travel through a wormhole in space in an attempt to ensure humanitys survival.', category_relationship = dramaCategory))
session.add(Item(title = 'Big Fish', description = 'A frustrated son tries to determine the fact from fiction in his dying fathers life.', category_relationship = dramaCategory))
session.add(Item(title = 'Hugo Cabret', description = 'In Paris in 1931, an orphan named Hugo Cabret, who lives in the walls of a train station, is wrapped up in a mystery involving his late father and an automaton.', category_relationship = dramaCategory))
session.add(Item(title = '127 Hours', description = 'An adventurous mountain climber becomes trapped under a boulder while canyoneering alone near Moab, Utah and resorts to desperate measures in order to survive.', category_relationship = dramaCategory))
session.commit()

#add fantasy items
session.add(Item(title = 'Avatar', description = 'A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.', category_relationship = fantasyCategory))
session.add(Item(title = 'Life of P', description = 'A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery. While cast away, he forms an unexpected connection with another survivor: a fearsome Bengal tiger.', category_relationship = fantasyCategory))
session.add(Item(title = 'Wonder Woman', description = 'When a pilot crashes and tells of conflict in the outside world, Diana, an Amazonian warrior in training, leaves home to fight a war, discovering her full powers and true destiny.', category_relationship = fantasyCategory))
session.add(Item(title = 'Pans Labyrinth', description = 'In the Falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world.', category_relationship = fantasyCategory))
session.commit()

#add horror items
session.add(Item(title = 'The Wailing', description = 'Soon after a stranger arrives in a little village, a mysterious sickness starts spreading. A policeman, drawn into the incident, is forced to solve the mystery in order to save his daughter.', category_relationship = horrorCategory))
session.add(Item(title = '28 Days Later...', description = 'Four weeks after a mysterious, incurable virus spreads throughout the UK, a handful of survivors try to find sanctuary.', category_relationship = horrorCategory))
session.add(Item(title = 'Conjuring', description = 'Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.', category_relationship = horrorCategory))
session.add(Item(title = 'A Quiet Place', description = 'In a post-apocalyptic world, a family is forced to live in silence while hiding from monsters with ultra-sensitive hearing.', category_relationship = horrorCategory))
session.commit()

#add thriller items
session.add(Item(title = 'Blood Diamond', description = 'A fisherman, a smuggler, and a syndicate of businessmen match wits over the possession of a priceless diamond.', category_relationship = thrillerCategory))
session.add(Item(title = 'Departed', description = 'An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.', category_relationship = thrillerCategory))
session.add(Item(title = 'Memento', description = 'A man with short-term memory loss attempts to track down his wifes murderer.', category_relationship = thrillerCategory))
session.add(Item(title = 'Eskiya', description = 'Baran the Bandit, released from prison after 35 years searches for vengeance and his lover.', category_relationship = thrillerCategory))
session.commit()

#check insert
print(session.query(Category).all())
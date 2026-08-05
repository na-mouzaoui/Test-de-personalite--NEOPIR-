import tkinter as tk
import random
from tkinter import ttk
import TNOTE
import re
import subprocess
import platform
import os
import sys
#import CALCUL
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from tempfile import NamedTemporaryFile
from reportlab.platypus import Image
from matplotlib.backends.backend_pdf import PdfPages
import tempfile

# Initialiser la fenêtre principale avec une taille constante
root = tk.Tk()



def get_resource_path(relative_path):
    """Retourne le chemin absolu d'une ressource, en gérant PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # Utilisé par PyInstaller pour le dossier temporaire
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Utilisez `get_resource_path` pour obtenir le chemin de l'icône
#icon_path = get_resource_path("logo.ico")
#root.iconbitmap(icon_path)
root.geometry("1100x550")  # Taille constante : 900x600 pixels
root.title("Test de Personnalité  V1.0.8")

# Liste des propositions
#propositions=["prest?"]
propositionsFR = [
  "Je ne suis pas du genre à me faire du souci",
  "J’aime vraiment bien la plupart des gens que je rencontre",
  "J’ai une imagination très active.",
  "J’ai tendance à être cynique et sceptique en ce qui concerne les intentions des autres",
  "Je suis réputé(e) pour ma prudence et mon bon sens",
  "Je me mets souvent en colère à cause de la manière dont les gens me traitent",
  "J’essaie d’éviter les foules.",
  "Les préoccupations esthétiques et artistiques ne sont pas très importantes pour moi",
  " Je ne suis ni rusé(e) ni sournois ( e )",
  "Je préfère me garder des possibilités de choix plutôt que tout planifier à l’avance",
  "Il est rare que je me sente trop seul(e) et cafardeux (se)",
  "Je suis autoritaire, énergique et je n’hésite pas à m’affirmer",
  "Sans émotions fortes, la vie serait sans intérêt pour moi",
  "Certains trouvent que je suis égoïste et que je ne pense qu’à moi",
  "J’essaie d’accomplir consciencieusement toutes les taches qui me sont confiées",
  "Quand j’ai affaire à d’autres personnes, je redoute toujours de faire une gaffe",
  "Dans le travail et dans les loisirs, je prends tout mon temps",
  "Je  suis bien installé( e ) dans mes habitudes",
  "Je préférerais coopérer avec les autres plutôt que me mettre en compétition",
  "Je suis nonchalant (e ) et pas très ambitieux (se)",
  "Je fais rarement des excès en quoi que ce soit",
  "J’ai souvent une forte envie de quelque chose qui romprait la monotonie",
  "Je prends souvent plaisir à jouer avec des théories ou des idées abstraites",
  "Cela ne me gêne pas de me vanter de mes talents et de ce que j’ai réalisé",
  "J’arrive assez bien à m’organiser pour faire les choses à temps",
  "Je me sens souvent désespéré(e) et je voudrais que quelqu’un d’autre résolve mes problèmes",
  "Je n’ai jamais sauté de joie au sens littéral du terme.",
  "Je crois que laisser les étudiants écouter des orateurs controversés ne peut que les embrouiller et les égarer",
  "Les dirigeants politiques doivent être plus attentifs à l’aspect humain de leur politique",
  "Au fil des années, j’ai fait un certain nombre de choses plutôt stupides",
  "Il est facile de me faire peur.",
  "Je n’ai pas beaucoup de plaisir à bavarder avec les gens",
  "j’essaie de maintenir toutes mes pensées dans une direction réaliste et d’éviter les envolées de l’imagination",
  "Je crois que la plupart des gens sont fondamentalement bien intentionnés",
  "Je ne prends pas les devoirs civiques, comme le vote, très au sérieux.",
  "Je suis une personne d’humeur égale",
  "J’aime avoir beaucoup de gens autour de moi.",
  "Il m’arrive quelquefois de m’absorber complètement dans la musique que j’écoute.",
  "Si c’est nécessaire, je suis disposé(e) à manipuler les gens pour obtenir ce que je veux",
  "Je maintiens mes affaires nettes et propres",
  "Quelquefois, je me sens complètement sans valeur",
  "Je ne m’affirme pas toujours autant que je devrais",
  "J’éprouve rarement des émotions fortes",
  "j’essaie d’être poli(e) avec chaque personne que je rencontre",
  "Il m’arrive parfois de ne pas tenir mes engagements ou de ne pas assumer mes responsabilités comme je le devrais",
  "Je me sens rarement mal à l’aise quand je suis avec des gens",
  "Quand je fais quelque chose, je le fais avec énergie",
  "Je pense qu’il est intéressant d’apprendre de nouvelles activités de loisir et de s’y perfectionner",
  "Je peux être sarcastique et cassant(e ) si besoin est",
  "J’ai un ensemble bien défini d’objectifs et je travaille pour les atteindre de façon ordonnée",
  "j’ai du mal à résister à mes désirs",
  "Je n’aimerais pas passer mes vacances à Las Vegas",
  "Je trouve les discussions philosophiques ennuyeuses",
  "Je préfère ne pas parler de moi-même  ni de ce que j’ai accompli",
  "Je perds beaucoup de temps avant de me mettre au travail",
  "Je me sens capable de faire face à la plupart de mes problèmes",
  "J’ai quelquefois éprouvé une joie intense ou de l’extase",
  "Je crois que les lois et les politiques sociales devraient changer pour refléter les besoins d’un monde qui  change",
  "J’ai la tête dure et je ne suis pas sentimental (e) dans mes attitudes",
  "j’examine les choses en  détail avant d’arriver à une décision",
  "Il est rare que je me sente craintif (Ve) ou anxieux (se)",
  "j’ai la réputation d’être une personne chaleureuse et amicale",
  "J’ai une vie imaginaire active",
  "Je crois que la plupart des gens vont profiter de vous si vous les laissez faire",
  "Je me tiens au courant et je prends habituellement des décisions intelligentes",
  "J’ai la réputation d’avoir le sang chaud et de me mettre facilement en colère",
  "Je préfère habituellement faire les choses seul ( e)",
  "Assister à des spectacles de ballet ou de danse moderne m’ennuie",
  "Je ne pourrais tromper personne, même si je le voulais",
  "Je ne suis pas quelqu’un de très méthodique",
  "Je suis rarement triste ou déprimé",
  "J’ai souvent dirigé les groupes auxquels j’ai  appartenu",
  "La manière dont je sens les choses est importante pour moi",
  "Certains me trouvent froid(e)et calculateur (trice)",
  "Je paie mes dettes rapidement et dans leur totalité",
  "Certaines fois, j’ai eu tellement honte que j’aurais voulu me cacher",
  "J’ai tendance à travailler lentement mais surement",
  "Une  fois que j’ai trouvé la bonne manière de faire quelque chose, je m’y tiens",
  "J’hésite à exprimer ma colère, même quand elle est justifiée",
  "Quand je commence un programme d’amélioration personnelle (par exemple : faire de la gymnastique, faire un régime, ou suivre une série de cours, etc.), j’abandonne habituellement au bout de quelques jours",
  "J’ai peu de difficulté à résister à la tentation",
  "Il m’est arrivé de faire des choses rien que pour l’excitation ou le frisson",
  "Je prends plaisir à résoudre des problèmes ou des énigmes",
  "Je suis meilleur(e) que la plupart des gens, et je le sais",
  "Je suis quelqu’un d’efficace qui vient toujours à bout du travail",
  "Quand je suis sous la pression de situation trop difficile, j’ai quelquefois l’impression que je vais m’effondrer",
  "Je ne suis pas un(e) optimiste souriant(e)",
  "Je crois que nous devrions nous tourner vers nos autorités religieuses pour les décisions concernant les questions morales",
  "On n’en fait jamais trop pour les pauvres et les personnes âgées",
  "Il m’arrive à l’occasion d’agir d’abord et de réfléchir ensuite",
  "Je me sens souvent tendu(e) et nerveux (se)",
  "Beaucoup de gens me trouvent assez froid(e) et distant ( e)",
  "Je n’aime pas perdre mon temps à rêvasser",
  "Je pense que la plupart des gens auxquels j’ai affaire sont honnêtes  et dignes de confiance",
  "Je me mets souvent dans des situations sans y être complètement préparé (e)",
  "On ne me considère pas comme une personne susceptible et ombrageuse",
  "J’ai vraiment besoin des autres si je reste longtemps seul(e )",
  "Je suis intrigué(e) par les formes et les motifs que je trouve dans l’art et dans le nature",
  "Etre parfaitement honnête est une mauvaise façon de faire des affaires",
  "J’aime bien garder chaque chose à sa place, comme cela je sais exactement ou elle est",
  "J’ai quelquefois éprouvé un sentiment profond de culpabilité ou de péché",
  "Dans les réunions, je laisse d’habitude les autres parlers",
  "Il est rare que j’accorde beaucoup d’attention à mes sentiments du moment",
  "J’essaie en général d’être attentionné(e) et prévenant (e)",
  "Il m’arrive de tricher quand je joue seul(e) (par exemple :quand je joue au solitaire, quand je fais des réussites,..Etc.)",
  "ça ne me gêne pas trop si les gens  se moquent de moi ou me taquinent",
  "J’ai souvent le sentiment de déborder d’énergie",
  "j’essaie souvent des plats nouveaux et exotiques",
  "Si je n’aime pas les gens, je le leur fais savoir",
  "Je travaille dur pour  atteindre mes objectifs",
  "Quand je suis devant mes plats favoris, j’ai tendance à trop manger",
  "J’ai tendance à éviter les films choquants ou effrayants",
  "Je perds quelquefois tout intérêt quand les gens parlent de sujets très abstraits et théoriques",
  "J’essaie d’être modeste",
  "J’ai du mal à me forcer à faire ce que je devrais",
  "Je garde la tête froide dans les situations d’urgence",
  "Quelquefois, je déborde de bonheur",
  "Je crois que les idées différentes du bon (bien, beau, vrai) et du mauvais (mal, laid, faux) que les gens ont dans d’autres sociétés peuvent être valables pour eux",
  "Je n’ai aucune sympathie pour les mendiants",
  "Avant d’agir, je réfléchis toujours aux conséquences de mon action",
  "Je ressens rarement de l’appréhension au sujet de l’avenir",
  "Je prends réellement plaisir à parler avec les gens",
  "Je prends plaisir à me concentrer sur une image intérieure ou une rêverie et à explorer toutes ses possibilités en les laissant croitre et à explorer toutes ses possibilités en les laissant croitre et se développer",
  "Je suis méfiant (e) quand quelqu’un fait quelque chose de gentil pour moi",
  "Je suis fier(e)de la sureté de mon jugement",
  "J’en arrive souvent à être  dégouté (e)par les gens auxquels je dois avoir affaire",
  "Je préfère un travail qui me permet de travailler seul(e) sans être embêté (e) par les autres",
  "La poésie a peu ou pas d’effet sur moi",
  "Je détesterais qu’on me prenne pour un(e) hypocrite",
  "Il me semble que je ne serai jamais capable de m’organiser",
  "J’ai tendance à me faire des reproche quand quelque chose va de travers",
  "Les autres se tournent souvent vers moi pour prendre des décisions",
  "j’éprouve une grande variété d’émotions ou de sentiments du moment",
  "Je n’ai pas la réputation d’être généreux (se)",
  "Quand je prends un engagement, on peut toujours compter sur moi pour aller jusqu’au bout.",
  "Je me sens souvent inférieur ( e) aux autres",
  "Je ne suis pas aussi rapide et dynamique que les autres",
  "Je préfère souvent passer mon temps dans un entourage familier",
  "Quand on m’a insulté (e), j’essaie simplement de pardonner et d’oublier",
  "Je ne ressens pas un besoin intense de promotion",
  "Je m’abandonne rarement à mes impulsions",
  " J’aime bien être là où il y a de l’action",
  "Je prends plaisir à travailler sur des énigmes du genre \"casse-tête\" ou \"sport cérébral\"",
  "J’ai une très haute opinion de moi-même",
  "Une fois que je démarre un projet, je le termine presque toujours",
  "Il est souvent difficile pour moi de prendre une décision",
  "Je ne me trouve pas particulièrement insouciant(e) et gai(e)",
  "Je crois que la fidélité à ses propres idéaux et principes  est plus importante que « l’ouverture d’esprit »",
  "Les besoins humains devraient toujours avoir la priorité sur les considérations économiques",
  "Je fais souvent des choses sur l’impulsion du moment.",
  "Je me fais souvent du souci à propos de choses qui pourraient mal tourner",
  "Je trouve facile de sourire et d’être agréable avec des inconnus",
  "Si je sens que  mon esprit commence à dériver vers des rêveries, j’ai l’habitude de m’occuper et de me mettre à me concentrer  sur un travail ou une activité",
  "Ma première réaction est de faire confiance aux gens",
  "Je n’ai pas l’impression de réussir complètement en quoi que ce soit",
  "Il en faut beaucoup pour me rendre furieux (se)",
  "Je préférerais des vacances sur une plage à la mode plutôt que dans une cabane isolée dans les bois",
  "Certains genres de musique exercent sur moi fascination sans fin",
  "Parfois, j’utilise la ruse pour amener les gens à faire ce que je veux",
  "J’ai tendance à être quelque peu méticuleux (se) et exigeant(e)",
  "J’ai une mauvaise opinion de moi-même",
  "Je préfère suivre mon propre chemin plutôt que diriger les autres",
  "Je remarque rarement les changements d’humeur  ou les sentiments que provoquent des environnements différents",
  "La plupart des gens que je connais m’aiment bien",
  "J’ai des principes moraux et j’y adhère strictement",
  "Je me sens à l’aise en présence de mes patrons ou d’autres autorités",
  "j’ai habituellement l’impression d’être pressé( e)",
  "je fais parfois des changements dans la maison, juste pour essayer quelque chose de différent",
  "Si quelqu`un provoque une bagarre, je suis prêt( e) à riposter.",
  " Je m’efforce de réussir tout ce que je peux",
  "Je mange quelquefois à m’en rendre malade",
  "J’adore le  frisson qu’on ressent sur les montagnes russes",
  "J’ai peu d’intérêt pour la réflexion sur la nature de l’univers ou sur la condition humaine",
  "Je n’ai pas l’impression d’être meilleur(e)que les autres, quelle que soit leur situation",
  "Quand un projet devient trop difficile, j’ai  tendance à en démarrer un autre",
  "Je me débrouille  assez bien dans une situation de crise",
  "Je suis une personne joyeuse et pleine de bonne humeur",
  "Je me trouve large d’esprit et tolérant(e)pour les façons de vivre des autres",
  "Je crois que tous les êtres humains sont dignes de respect",
  "Il est rare que je prenne des décisions hâtives",
  "j’ai moins de peurs que la plupart des gens",
  "J’ai des liens affectifs forts avec mes amis",
  "Quand j’étais enfant, il était rare que je prenne plaisir à « jouer à faire semblant",
  "J’ai tendance à supposer le meilleur chez les gens",
  "Je suis quelqu’un de très compétent",
  "Il m'est parfois arrivé d'être amer(ère) et plien(e ) de ressentiment.",
  "Habituellement, les réunions qui rassemblent un grand nombre de personnes m’ennuient",
  " Quelquefois, quand je lis de la poésie ou quand je regarde une œuvre d’art, je ressens un frisson ou j’ai la chair de poule",
  "il m’arrive de faire aux gens ce que je veux en les menaçant  ou en les flattant",
  "Je ne suis pas un(e)maniaque du nettoyage",
  "Quelquefois, les choses me semblent plutôt mornes et sans espoir",
  "Dans les conversations, j’ai tendance à parler plus que les autres.",
  "Je trouve facile d’avoir de l’empathie, c’est –à-dire de ressentir moi-même ce que les autres ressentent",
  "Je me considère comme une personne charitable",
  "Ce que je fais, j’essaie de le faire soigneusement, comme ça il n’ya pas a le refaire",
  "Si j’ai dit ou fait quelque chose de mal à quelqu’un, je peux à peine supporter de le regarder en face à nouveau",
  " Mon rythme de vie est rapide",
  " En vacances, je préfère retourner dans un endroit que je connais bien plutôt qu’aller dans un nouvel endroit",
  "Je suis dur(e) et inflexible",
  "Je m’efforce à l’excellence dans tout ce que je fais",
  "Quelquefois, je fais sur une impulsion des choses que je regrette par la suite",
  "Je suis attiré(e)par les  couleurs vives et les styles voyants",
  "J’ai beaucoup de curiosité intellectuelle",
  "j’aime mieux faire l’éloge des autres plutôt que recevoir moi-même des éloges",
  "Il y a tant de petits travaux qu’il faudrait faire que parfois, tout simplement je les ignore tous",
  "Quand tout a l’air d’aller de travers, je reste capable de prendre les bonnes décisions",
  "J’emploie rarement des mots tels que « fantastique » ou « sensationnel » pour décrire ce qui m’est arrivé",
  "Je pense que si les gens ne savent pas à quoi ils croient quand ils ont vingt-cinq ans il ya quelque chose qui ne tourne pas rond chez eux",
  "J’ai de la compassion pour ceux qui ont moins de chance que moi",
  "Quand je pars en voyage, je prépare à l’avance un programme minutieux",
  "Des pensées effrayantes s’introduisent quelquefois dans ma tête",
  "Je m’intéresse vraiment aux gens avec lesquels je travaille",
  "J’aurais du mal à laisser simplement mon esprit vagabonder sans contrôle ni direction",
  "j’ai une grande confiance dans la nature humaine",
  "Je suis efficace et productif (ve) dans mon travail.",
  "Pour moi, même des petites contrariétés peuvent être irritantes",
  "J’aime les «  fêtes » avec plein de gens",
  "J’aime lire de la poésie qui met l’accent sur les sentiments et  les images plutôt que sur le déroulement de l’histoire",
  "Je suis fier(ère) de l’habileté avec laquelle je manipule les gens",
  "Je passe beaucoup de temps à chercher des choses que j’ai mal rangées",
  " trop souvent, quand les choses vont mal, je me décourage et j’ai envie d’abandonner",
  "Je ne trouve pas facile de prendre une situation en main",
  " Des choses étranges – comme certains parfums ou des noms d’endroits lointains – peuvent provoquer en moi des émotions puissantes",
  "Si je peux, je fais un effort pour aider les autres",
  "Il faudrait réellement que je sois malade pour manquer une journée du travail",
  "Quand des gens que je connais fond des choses idiotes, j’en suis gêné(e) pour eux",
  "Je suis une personne très active.",
  " Je prends toujours le même chemin quand je vais quelque part.",
  "Je m’engage souvent dans des disputes avec ma famille ou mes collègues de travail",
  "Je consacre trop de temps au travail en négligeant la famille, les aimes et les loisirs",
  "Je suis toujours capable de garder le contrôle de mes sentiments",
  "J’aime bien faire partie de la foule dans les manifestations sportives",
  "j’ai une grande variété d’intérêts intellectuels",
  "Je suis quelqu’un de supérieur",
  "J’ai beaucoup d’autodiscipline",
  "Je suis assez stable émotionnellement",
  "Je ris facilement",
  "Je crois que la «  nouvelle morale » à base de permissivité n’est pas du tout une morale",
  "Je préférerais avoir la réputation de pardonner plutôt que celle d’être juste",
  "Avant de répondre à une question, j’y réfléchis à deux fois"
]


propositionsAR= [
    "لست من النوع القلق",
    "أنا حقا أحب معظم الناس الذين أقابلهم",
    "لدي خيال جد نشط",
    "لدي الطبع في أن أكون متشائم ومشكك في نوايا الآخرين",
    "أنا معروف بتوخي الحذر والحس السليم",
    "أغضب عادة بسبب طريقة معاملة الآخرين لي",
    "أحاول تجنب  حشد الجماهير (التجمعات)",
    "الاهتمامات الجمالية والفنية ليسوا مهمين بالنسبة لي",
    "لست مخادعا ولست خبيثا",
    "أفضل ترك الاحتمالات في اختياراتي بدلا من التخطيط المسبق",
    "نادرا ما أشعر بالوحدة والكآبة",
    "أنا متسلط وذو طاقة كبيرة ولا أتردد في فرض نفسي",
    "بدون مشاعر قوية، الحياة تصبح بالنسبة لي بدون معنى",
    "هناك من يرى أني أناني ولا أفكر سوى في نفسي",
    "أحاول القيام بكل وعي المهام الموكلة إلي",
    "عندما أتعامل مع أشخاص آخرين، أخشى دائما القيام بخطأ",
    "في العمل وفي الراحة أقوم بأخذ كامل وقتي",
    "أنا متمسك كثيرا بنشاطي المعتاد",
    "أفضل التعاون مع الآخرين على أن أكون في منافسة معهم",
    "أنا غير مبالي وغير طموح",
    "نادرا ما أقوم بإفراط في شيء ما",
    "لدي في كثير من الأحيان الرغبة في القيام بشيء يغير من عاداتي اليومية",
    "أجد المتعة في التعامل مع النظريات والأفكار المجردة",
    "لا يزعجني التفاخر بمواهبي وبالأشياء التي حققتها",
    "أستطيع أن أنظم نفسي للقيام بالأشياء في الوقت المحدد",
    "أشعر غالبا باليأس وأود أن يقوم شخص آخر بحل مشاكلي",
    "لم أقفز من شدة الفرح بمعنى الحقيقي",
    "أظن أن ترك الطلاب يسمعون لمحاضرات جدلية لا يؤديهم إلى الخلط والضياع",
    "الزعماء السياسيين يجب أن يكونوا منتبهين للمظهر الإنساني لسياستهم",
    "مع مرور السنين قمت بأشياء حقا غبية",
    "من السهل جعلي أخاف",
    "لا أجد متعة كبيرة في الثرثرة مع الآخرين",
    "أحاول الحفاظ على أفكاري واقعية وأجتنب كثيرا استعمال الخيال",
    "أظن أن معظم الأشخاص في جوهرهم حسنوا النية",
    "لا أتخذ الواجبات المدنية مثل الانتخابات بجد",
    "أنا شخص ذو مزاج عادل",
    "أحب أن أكون محاطا بالآخرين",
    "يحدث لي أحيانا أن أستغرق تماما في الموسيقى التي أستمع لها",
    "إن كان من الضروري، أنا مستعد للتلاعب بالآخرين من أجل التحصل على ما أريد",
    "أبقي على أعمالي نظيفة ومرتبة",
    "أحيانا لا أشعر بأن لدي قيمة",
    "لا أفرض نفسي كما ينبغي علي فعله",
    "أنا نادرا ما تراودني مشاعر قوية",
    "أحاول أن أكون مهذبا مع كل شخص ألتقي به",
    "أنا في بعض الأحيان لا ألتزم بوعودي ولا أتحمل مسؤولياتي كما أريد",
    "أشعر نادرا بعدم الراحة عندما أكون مع الناس",
    "عندما أفعل شيئا فاتني أقوم به بحيوية",
    "أعتقد أنه من المهم تعلم نشاط جديد للترفيه مع تحسينه",
    "يمكن أن أكون ساخرًا ومستهزئًا عند الحاجة",
    "لدي مجموعة من الأهداف وأسعى لتحقيقها بصفة منظمة",
    "أجد صعوبة التحكم في رغباتي",
    "أنا لا أحب قضاء عطلتي في لاس فيغاس",
    "أجد المناقشات الفلسفية مملة",
    "أفضل ألا أتكلم عن نفسي وما وصلت إليه",
    "فقدت الكثير من الوقت قبل الشروع في عمل",
    "أشعر أنني قادر على التعامل مع جميع مشاكلي",
    "أنا أحيانا أشعر بنشوة وسعادة كبيرة",
    "أعتقد أن القوانين والسياسة الاجتماعية يجب أن تتغير لأن العالم يتغير",
    "أنا لا أغير وجهة نظري وكما أنني لست عاطفيا في مواقفي",
    "أنا أنظر إلى الأشياء بالتفصيل قبل التوصل إلى قرار",
    "من النادر أن أشعر بالخوف والقلق",
    "لدي سمعة في كوني شخص دافئ وودي",
    "لدي حياة خيالية نشيطة",
    "أعتقد أن معظم الناس يستغلونك إذا تتركهم يفعلون ذلك",
    "أحرس على تحيين معلوماتي وعادة ما أقوم باتخاذ قرارات ذكية",
    "لدي سمعة بأنني أغضب بسهولة",
    "عادة أنا أفضل فعل الأشياء وحيدا",
    "حضور عروض الباليه أو الرقص الحديث يشعرني بالملل",
    "لا يمكنني خداع أي أحد حتى ولو أردت ذلك",
    "أنا لست منهجيا",
    "أنا نادرا ما أشعر بالحزن أو الاكتئاب",
    "كثيرا ما كنت قائدا للمجموعات التي أنتمي إليها",
    "طريقتي في الشعور بالأشياء مهمة بالنسبة لي",
    "البعض يجدني باردا ومحاسبا لكل شيء",
    "أدفع ديوني بسرعة وفي مجملها",
    "في بعض الأحيان أشعر حقا بالخجل لدرجة أنني أردت الاختباء",
    "أنا أميل للعمل ببطء ولكن بفعالية",
    "عندما أجد الطريقة الصحيحة لفعل شيء ما أتبعها مباشرة",
    "أتردد في التعبير عن غضبي، حتى ولو كان مبررا",
    "عندما أبدأ برنامج في التحسين الذاتي (مثال: القيام بالجمباز، اتباع نظام غذائي أو اتباع مجموعة من الدورات)، عادة ما أتخلى عن النشاط بعد مرور بعض الأيام",
    "أجد صعوبة في مقاومة الإغراء",
    "حدث لي أن قمت بأشياء فقط لمجرد الإثارة أو التشويق",
    "أجد متعة في حل المشاكل أو الألغاز",
    "أنا أفضل من معظم الناس وأنا أعلم بذلك",
    "أنا شخص فعال وأنهي دائما عملي",
    "عندما أكون تحت الضغط في مواقف صعبة، في بعض الأحيان أشعر بأنني سأنهار",
    "أنا لست متفائلا وضاحكا",
    "أعتقد أنه يجب أن ننظر إلى السلطات الدينية فيما يخص المشاكل الأخلاقية",
    "نحن لم نفعل مطلقا الكثير للفقراء والمسنين",
    "يحدث لي أحيانا العمل أولا ثم التفكير لاحقا",
    "كثيرا ما أشعر بالتوتر والعصبية",
    "يجد كثير من الناس أني متحفظ وغير ودي",
    "أنا لا أحب إضاعة الوقت في أحلام اليقظة",
    "أعتقد أن معظم الناس الذي أتعامل معها صادقةوجديرة بالثقة",
    "كثيرا ما أضع نفسي في مواقف دون أن أكون على استعداد كامل لها",
    "لا يعتبرني الغير كشخص سريع الغضب وشديد الحساسية",
    "أنا حقا في حاجة للآخرين إذا بقيت فترة طويلة وحدي",
    "أنا مفتون بالنماذج وأنماط الفن التي أجدها في الطبيعة",
    "أن تكون صادقا تماما هو وسيلة سيئة للقيام بالأعمال",
    "أود أن أبقي كل شيء في مكانه، هكذا أنا أعلم تماما أين هو",
    "تراودني في بعض الأحيان أحاسيس عميقة بالذنب أو بالخطيئة",
    "في الاجتماعات، عادة ما أدع الآخرين يتكلمون",
    "من النادر أن أعطي الكثير من الانتباه لإحساساتي في الوقت الحاضر",
    "أحاول بشكل عام أن أكون مهتم ومنتبها",
    "أحيانا أغش عندما ألعب لوحدي",
    "لا يزعجني كثيرا إذا كان الناس يسخرون مني",
    "كثيرا ما أشعر بأنني ملئ بالطاقة",
    "أحاول دائما أن أطبخ طبق جديد وغريب",
    "إذا لم أحب الناس، أظهر لهم ذلك",
    "أنا أعمل بجد لتحقيق أهدافي",
    "عندما أكون أمام أطباقي المفضلة، لدي ميل في الأكل كثيرا",
    "أنا أميل لتجنب الأفلام المروعة والمخيفة",
    "في بعض الأحيان أعطي كل الاهتمام للناس الذين يتحدثون عن مواضيع مجردة للغاية ونظرية",
    "أنا أحاول أن أكون متواضعا",
    "لدي صعوبة في القيام بالأشياء التي يجب القيام بها",
    "أنا هادئ في حالات الطوارئ",
    "في بعض الأحيان، أمتلئ بالسعادة",
    "أعتقد أن الأفكار المختلفة عن الخير والشر والتي لدى الأفراد في مجتمعات أخرى يمكن أن تكون صالحة بالنسبة لهم",
    "ليس لدي أي تعاطف للمتسولين",
    "قبل التصرف، أفكر دائما في عواقب أعمالي",
    "أنا نادرا ما أشعر بالخوف حول المستقبل",
    "أنا في الواقع، أجد متعة في الحديث مع الناس",
    "أنا أجد متعة في التركيز على صورة داخلية أو خيالية وأن أستكشف كل إمكانياتها مع ترك لها المساحة لتطوير",
    "أنا حذر عندما يقوم شخص ما بفعل شيء لطيف بالنسبة لي",
    "أنا أعتزّ بصفاء حكمي",
    "كثيرا ما ينتابني الاشمئزاز من الناس الذين أتعامل معهم",
    "أفضل العمل الذي يسمح لي بالعمل لوحدي دون أن يزعجني الآخرون",
    "الشعر ليس له تأثير علي",
    "أكره أن يُؤخذ عني نظرة المنافق",
    "أعتقد أنني لا أستطيع أن أكون منظما",
    "أنا أميل إلى لوم نفسي عندما يكون هناك شيء على غير ما يرام",
    "الناس دائما تأخذ نصيحتي لاتخاذ القرار",
    "أشعر بمجموعة متنوعة من المشاعر أو العواطف",
    "ليس لدي سمعة كوني كريم",
    "عندما آخذ التزام، يمكن دائما الاعتماد علي للذهاب إلى النهاية",
    "كثيرا ما أشعر أني أقل شأنا من الآخرين",
    "أنا لست سريعًا بما فيه الكفاية وحيوي كما هم الآخرون",
    "أنا أفضل قضاء وقتي في بيئة أسرية",
    "عند أي إهانة لي أحاول ببساطة أن أسامح وأنسى",
    "لا أشعر بحاجة ملحة لأي تعزيز لحاجاتي",
    "نادرا ما أترك دوافعي تحكم في شخصيتي",
    "لا أحب أن أكون في المواقع الزاخرة بالأحداث",
    "يسرني حل الألغاز الصعبة",
    "رأيي في نفسي عالي جدا",
    "بمجرد أن أبدأ مشروعا، أنهيه تقريبا دائما",
    "غالبا ما يكون من الصعب بالنسبة لي اتخاذ قرار",
    "أنا لا أجد نفسي بشكل خاص مبتهجً وغير مهتم",
    "أعتقد أن الولاء لمبادئه الخاصة أكثر أهمية من حرية الفكر",
    "الاحتياجات الإنسانية يجب أن يكون لديها الأولوية دائما على الاعتبارات الاقتصادية",
    "كثيرا ما أفعل أشياء على الرغبة الراهنة",
    "أنا غالبا قلق بشأن الأشياء التي يمكن أن تنقلب بطريقة سيئة",
    "أجد أنه من السهل أن أبتسم وأكون لطيفً مع المجهولين",
    "إذا وجدت أن فكري بدأ في الانصراف لأحلام اليقظة، لدي عادة في أن أركز على عمل ما أو على نشاط آخر",
    "رد فعلي الأول هو أن أثق بالناس",
    "لا أشعر بنجاح تام في أي شيء أنجزه",
    "من الصعب جدًا أن أغضب",
    "أفضل العطلة على الشاطئ على منزل معزول في الغابات",
    "تُثير بعض الأنماط الموسيقية في نفسي افتتانًا لا حدود له",
    "أحيانا ألجأ إلى الحيلة لكي يفعل الناس ما أريده",
    "أنا أميل إلى أن أكون دقيقًا وكثير المطالب",
    "تقييمي لذاتي سلبي",
    "أفضل أن أتتبع مساري بدلًا من أن أوجه الآخرين",
    "أنا نادرا ما ألاحظ تغيرات في المزاج أو المشاعر التي تسببها بيانات مختلفة",
    "معظم الناس الذين أعرفهم يحبونني",
    "لدي مبادئ أخلاقية وأنا أوافقها بصرامة",
    "أشعر بالراحة في حضور المدير أو المسؤول الذي أعمل معه",
    "عادة ما أشعر أنني مضغوط",
    "في بعض الأحيان أحدث تغييرًا في المنزل، فقط من أجل تجربة شيء مختلف",
    "إذا تسبب شخص ما في معركة، أنا مستعد للرد",
    "إني أحاول تحقيق كل ما بوسعي",
    "في بعض الأحيان أكل عدة مرات يجعلني مريضًا",
    "أحب الإثارة التي نشعر بها في لعبة الجبال الروسية(Montagne Russes)",
    "لدي القليل من الاهتمام في التفكير في طبيعة الكون والأوضاع الإنسانية",
    "لم أشعر أني أفضل من غيري أيا كانت الوضعية",
    "عندما يصبح مشروع صعبًا جدًا، أنا أميل لبدء آخر",
    "أسير الأمور بشكل جيد جدًا في حالة الأزمات",
    "أنا شخص مرح وذو مزاج جيد",
    "أجد نفسي متفهمًا وأتقبل آراء ونمط حياة الآخرين",
    "أعتقد أن جميع البشر يستحقون الاحترام",
    "من النادر أن أتخذ قرارًا متسرعًا",
    "لدي خوف أقل من معظم الناس",
    "لدي علاقات قوية مع أصدقائي",
    "عندما كنت طفلاً، فمن النادر أن يسرني التظاهر في اللعب",
    "أميل للافتراض ما في الناس من الأفضل",
    "أنا شخص كفء جدًا",
    "حدث لي أن كنت محبوبًا ومملوءًا بالحقد",
    "تشعرني الاجتماعات التي تحتوي عددًا كبيرًا من الناس بالملل",
    "في بعض الأحيان عندما أقرأ الشعر أو أشاهد عملًا فنيًا أشعر بالقشعريرة",
    "أفعل أحيانًا للناس ما أريده عن طريق تهديدهم أو إغرائهم",
    "أنا ليس لدي الهوس في النظافة",
    "أحيانًا تبدو الأمور قاتمة وميؤوس منها",
    "في الحوار لدي ميل للحديث أكثر من الآخرين",
    "أجد من السهل أن أكون متعاطفًا، بمعنى أستطيع الشعور بما يشعر به الآخرون",
    "أعتبر نفسي شخصًا غير أناني",
    "ما أقوم به، أحاول القيام به بعناية",
    "إذا قلت أو فعلت شيئًا خاطئًا لشخص ما فإنني أكاد لا أتحمل النظر إليه مباشرة من جديد",
    "نمط حياتي سريع",
    "في الإجازة أفضل العودة إلى مكان أعرفه جيدًا بدلًا من أن أذهب إلى مكان جديد",
    "أنا صارم وغير مرن",
    "أسعى إلى التميّز في كل ما أقوم به",
    "في بعض الأحيان في لحظة اندفاع أقوم بأشياء أندم عليها لاحقًا",
    "أنجذب إلى الألوان الزاهية والأساليب الملفتة",
    "لدي الكثير من الفضول الفكري",
    "أفضل مدح الآخرين بدلًا من الحصول على مدحهم",
    "هناك الكثير من الأعمال الصغيرة التي يجب القيام بها، أحيانا بكل بساطة أقوم بتجاهلها كلها",
    "عندما يبدو أن كل شيء على غير ما يرام، أبقى قادرًا على اتخاذ القرارات الصائبة",
    "نادرا ما أستخدم كلمات مثل مذهل أو مثير من أجل وصف ما يحدث لي",
    "أعتقد أنّه إذا كان الناس لا يعرفون بماذا يؤمنون عندما يبلغون الخامسة والعشرين، فهناك شيء غير سليم عندهم",
    "أشفق على أولئك الذين هم أقل حظًا مني",
    "عندما أذهب في رحلة، أحضر مسبقًا برنامجًا دقيقًا",
    "تخطر أحيانًا في ذهني أفكار مرعبة",
    "أهتم حقًا بالأشخاص الذين أعمل معهم",
    "أجد صعوبة في ترك ذهني يطوف (يجول) بدون رقابة أو تسير",
    "لدي ثقة كبيرة في طبيعة البشر",
    "أنا فعال ومنتج في عملي",
    "بالنسبة لي، حتى اإلزعاجات البسيطة يمكن أن تكون سبب الاستثارة",
    "أحب الحفلات المليئة بالأشخاص",
    "أحب قراءة الشعر الذي يركز على المشاعر والصور بدلًا من الذي يركز على سيرورة التاريخ",
    "أفتخر بالمهارة التي أتعامل بها مع الناس",
    "لا أقضي وقتًا طويلاً في البحث على الأشياء التي وضعتها في غير محلها",
    "في كثير من الأحيان عندما تسوء الأمور أفشل وتكون لدي الرغبة في الانسحاب",
    "لا أجد من السهل التحكم في الوضعيات (التحكم في زمام الأمور)",
    "أشياء غريبة (مثل بعض الروائح أو أسماء بعض الأماكن) يمكن أن تثير عواطفي",
    "إذا استطعت، سأبذل جهدا من أجل مساعدة الآخرين",
    "يجب أن أكون حقًا مريضًا لأغيب يومًا عن العمل",
    "عندما يقوم الأشخاص الذين أعرفهم بأشياء سخيفة، أشعر بالحرج من أجلهم",
    "أنا شخص نشط جدًا",
    "أتخذ دائمًا نفس الطريق عندما أذهب لمكان ما",
    "أدخل غالبًا في خلافات مع عائلتي وزملائي في العمل",
    "أنشغل بالعمل إلى حدّ إهمال الأسرة والأصدقاء والراحة",
    "أنا دائمًا قادر على التحكم في مشاعري",
    "أحب أن أكون جزءًا من الحشد في الأحداث الرياضية",
    "لدي مجموعة متنوعة واسعة من المنافع الفكرية",
    "أنا شخص ذو مكانة عالية",
    "لدي الكثير من الانضباط الذاتي",
    "أنا مستقر عاطفيًا بما فيه الكفاية",
    "أنا أضحك بسهولة",
    "أظن أن المبادئ الأخلاقية الجديدة التي تقوم على أساس التساهل، لا تعتبر إطلاقًا من الأخلاق",
    "أفضل أن تكون لدي القدرة على التسامح على أن أكون عادلاً",
    "أفكر كثيرًا قبل الإجابة على سؤال ما"
]

responses = []  # Liste pour enregistrer les réponses
current_proposition = 0  # Indice de la proposition actuelle
selected_language = "FR"  # Langue sélectionnée par défaut

# Variables pour les informations personnelles
nom = tk.StringVar()
prenom = tk.StringVar()
age = tk.StringVar()
sexe = tk.StringVar()

# Dictionnaires pour les textes de l'interface selon la langue
texts = {
    "FR": {
        "welcome": "Bienvenue au test de personnalité",
        "description": "Ce test va vous permettre de mieux comprendre votre personnalité.\nVous allez répondre à plusieurs propositions en indiquant votre degré d'accord sur une échelle de 1 à 5.",
        "language_choice": "Choisissez votre langue / اختر لغتك:",
        "french": "Français",
        "arabic": "العربية",
        "continue": "Continuer",
        "personal_info": "Veuillez entrer vos informations personnelles",
        "name": "Nom :",
        "firstname": "Prénom :",
        "age": "Âge :",
        "gender": "Sexe :",
        "male": "Homme",
        "female": "Femme",
        "fill_all_fields": "Veuillez remplir tous les champs avant de continuer.",
        "age_error": "L'âge doit être un nombre.",
        "name_error": "Le nom ne peut contenir que des CHOIX_REPs et des tirets.",
        "firstname_error": "Le prénom ne peut contenir que des CHOIX_REPs et des tirets.",
        "explanation_title": "Chaque proposition vous demande de donner votre avis sur une échelle de 1 à 5 :",
        "scale_1": "1 - Pas du tout d'accord",
        "scale_2": "2 - Pas d'accord", 
        "scale_3": "3 - Neutre",
        "scale_4": "4 - D'accord",
        "scale_5": "5 - Tout à fait d'accord",
        "start_test": "Commencer le test",
        "proposition": "Proposition",
        "option_1": "Pas du tout d'accord",
        "option_2": "Pas d'accord",
        "option_3": "Neutre",
        "option_4": "D'accord",
        "option_5": "Tout à fait d'accord",
        "next_proposition": "Proposition Suivante",
        "select_option": "Veuillez sélectionner une option avant de continuer.",
        "test_complete": "Merci d'avoir complété le test !",
        "show_report": "Afficher le rapport"
    },
    "AR": {
        "welcome": "مرحبا بكم في اختبار الشخصية",
        "description": "سيساعدك هذا الاختبار على فهم شخصيتك بشكل أفضل.\nستجيب على عدة عبارات بتحديد درجة موافقتك على مقياس من 1 إلى 5.",
        "language_choice": "Choisissez votre langue / اختر لغتك:",
        "french": "Français",
        "arabic": "العربية",
        "continue": "متابعة",
        "personal_info": "الرجاء إدخال معلوماتك الشخصية",
        "name": "اللقب :",
        "firstname": "الاسم  :",
        "age": "العمر :",
        "gender": "الجنس :",
        "male": "ذكر",
        "female": "أنثى",
        "fill_all_fields": "يرجى ملء جميع الحقول قبل المتابعة.",
        "age_error": "يجب أن يكون العمر رقماً.",
        "name_error": "لا يمكن أن يحتوي اللقب إلا على أحرف .",
        "firstname_error": "لا يمكن أن يحتوي الاسم إلا على أحرف .",
        "explanation_title": "كل عبارة تطلب منك إعطاء رأيك على مقياس من 1 إلى 5 :",
        "scale_1": "1 - غير موافق إطلاقاً",
        "scale_2": "2 - غير موافق",
        "scale_3": "3 - حيادي",
        "scale_4": "4 - موافق",
        "scale_5": "5 - موافق تماماً",
        "start_test": "بدء الاختبار",
        "proposition": "العبارة",
        "option_1": "غير موافق إطلاقاً",
        "option_2": "غير موافق",
        "option_3": "حيادي",
        "option_4": "موافق",
        "option_5": "موافق تماماً",
        "next_proposition": "العبارة التالية",
        "select_option": "يرجى اختيار خيار قبل المتابعة.",
        "test_complete": "شكراً لك لإكمال الاختبار!",
        "show_report": "عرض التقرير"
    }
}

# Fonction pour nettoyer la fenêtre
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Écran d'introduction
def introduction_screen():
    clear_window()

    # Titre de bienvenue
    label_intro = tk.Label(root, text=texts[selected_language]["welcome"], font=("Helvetica", 18), padx=20, pady=30)
    label_intro.pack()

    # Description
    label_description = tk.Label(root, text=texts[selected_language]["description"], font=("Helvetica", 12), padx=20, pady=20)
    label_description.pack()

    # Cadre pour le choix de langue
    language_frame = tk.Frame(root)
    language_frame.pack(pady=30)
    
    # Label pour le choix de langue
    label_language = tk.Label(language_frame, text=texts[selected_language]["language_choice"], font=("Helvetica", 14, "bold"))
    label_language.pack(pady=10)
    
    # Variable pour stocker la langue sélectionnée
    language_var = tk.StringVar(value=selected_language)
    
    # Boutons radio pour le choix de langue
    style = ttk.Style()
    style.configure("TRadiobutton", font=("Helvetica", 12))
    
    radio_french = ttk.Radiobutton(language_frame, text=texts["FR"]["french"], variable=language_var, value="FR", style="TRadiobutton")
    radio_french.pack(pady=5)
    
    radio_arabic = ttk.Radiobutton(language_frame, text=texts["AR"]["arabic"], variable=language_var, value="AR", style="TRadiobutton")
    radio_arabic.pack(pady=5)

    # Bouton continuer
    button_continue = ttk.Button(root, text=texts[selected_language]["continue"], command=lambda: set_language_and_continue(language_var.get()), width=20)
    button_continue.pack(side=tk.BOTTOM, pady=20)

def set_language_and_continue(selected_lang):
    global selected_language
    selected_language = selected_lang
    formulaire_screen()

def formulaire_screen():
    clear_window()
    sexe.set("")
    
    # Cadre principal au centre de la fenêtre
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(expand=True)  # Centre le cadre principal dans la fenêtre

    # Titre
    label_info = tk.Label(main_frame, text=texts[selected_language]["personal_info"], font=("Helvetica", 16, "bold"))
    label_info.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Champ "Nom"
    label_nom = ttk.Label(main_frame, text=texts[selected_language]["name"], font=("Helvetica", 12))
    label_nom.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
    entry_nom = ttk.Entry(main_frame, textvariable=nom, font=("Helvetica", 12), width=20)  # Réduit la largeur
    entry_nom.grid(row=1, column=1, pady=5, sticky="w")

    # Champ "Prénom"
    label_prenom = ttk.Label(main_frame, text=texts[selected_language]["firstname"], font=("Helvetica", 12))
    label_prenom.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
    entry_prenom = ttk.Entry(main_frame, textvariable=prenom, font=("Helvetica", 12), width=20)  # Réduit la largeur
    entry_prenom.grid(row=2, column=1, pady=5, sticky="w")

    # Champ "Âge"
    label_age = ttk.Label(main_frame, text=texts[selected_language]["age"], font=("Helvetica", 12))
    label_age.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=5)
    entry_age = ttk.Entry(main_frame, textvariable=age, font=("Helvetica", 12), width=20)  # Réduit la largeur
    entry_age.grid(row=3, column=1, pady=5, sticky="w")

    # Champ "Sexe" avec boutons radio
    label_sexe = ttk.Label(main_frame, text=texts[selected_language]["gender"], font=("Helvetica", 12))
    label_sexe.grid(row=4, column=0, sticky="e", padx=(0, 10), pady=(15, 5))

    frame_sexe = tk.Frame(main_frame)
    frame_sexe.grid(row=4, column=1, sticky="w")

    # Boutons radio pour le sexe
    style = ttk.Style()
    style.configure("TRadiobutton", font=("Helvetica", 12))

    bouton_homme = ttk.Radiobutton(frame_sexe, text=texts[selected_language]["male"], variable=sexe, value="H", style="TRadiobutton")
    bouton_homme.pack(side=tk.LEFT, padx=10)

    bouton_femme = ttk.Radiobutton(frame_sexe, text=texts[selected_language]["female"], variable=sexe, value="F", style="TRadiobutton")
    bouton_femme.pack(side=tk.LEFT, padx=10)

    # Bouton "Continuer" en bas, centré
    button_continue = ttk.Button(main_frame, text=texts[selected_language]["continue"], command=check_formulaire, width=20)
    button_continue.grid(row=5, column=0, columnspan=2, pady=(20, 0))

# Vérifier si les champs du formulaire sont remplis avant de continuer
def check_formulaire():
    # Vérification des champs vides
    if not nom.get() or not prenom.get() or not age.get() or not sexe.get():
        label_warning = tk.Label(root, text=texts[selected_language]["fill_all_fields"], fg="red", pady=10, padx=20)
        label_warning.pack()
        return

    # Vérification de l'âge
    try:
        age_value = int(age.get())
        if age_value < 0 or age_value > 99:
            raise ValueError
    except ValueError:
        label_warning = tk.Label(root, text=texts[selected_language]["age_error"], fg="red", pady=10, padx=20)
        label_warning.pack()
        return

    # Vérification du nom
    if not re.match("^[A-Za-zÀ-ÿ '-]+$", nom.get()):
        label_warning = tk.Label(root, text=texts[selected_language]["name_error"], fg="red", pady=10, padx=20)
        label_warning.pack()
        return

    # Vérification du prénom
    if not re.match("^[A-Za-zÀ-ÿ '-]+$", prenom.get()):
        label_warning = tk.Label(root, text=texts[selected_language]["firstname_error"], fg="red", pady=10, padx=20)
        label_warning.pack()
        return

    explanation_screen()  # Passer à l'écran d'explication si tout est valide

# Écran d'explication
def explanation_screen():
    clear_window()

    explanation_text = f"{texts[selected_language]['explanation_title']}\n\n\n" \
                      f"{texts[selected_language]['scale_1']}\n\n" \
                      f"{texts[selected_language]['scale_2']}\n\n" \
                      f"{texts[selected_language]['scale_3']}\n\n" \
                      f"{texts[selected_language]['scale_4']}\n\n" \
                      f"{texts[selected_language]['scale_5']}"

    label_explanation = tk.Label(root, text=explanation_text, font=("Helvetica", 12), padx=20, pady=120)
    label_explanation.pack()

    button_start = ttk.Button(root, text=texts[selected_language]["start_test"], command=start_test, width=20)
    button_start.pack(side=tk.BOTTOM, pady=20)  # Bouton aligné en bas

# Démarrage du test
def start_test():
    global current_proposition
    current_proposition = 0
    clear_window()
    show_proposition()

# Afficher une proposition
def show_proposition():
    clear_window()

    # Choisir la liste de propositions selon la langue
    propositions = propositionsFR if selected_language == "FR" else propositionsAR

    if current_proposition < len(propositions):
        proposition_text = f"{texts[selected_language]['proposition']} {current_proposition + 1}: {propositions[current_proposition]}"
        label_proposition = tk.Label(root, text=proposition_text, font=("Helvetica", 14), wraplength=800, padx=50, pady=120)
        label_proposition.pack()

        # Variable pour enregistrer la sélection de l'utilisateur
        selected_value = tk.IntVar(value=0)

        # Créer un frame pour organiser les boutons radio horizontalement
        frame_radio = tk.Frame(root)
        frame_radio.pack(pady=20)

        # Liste des textes pour les boutons radio selon la langue
        options = [
            texts[selected_language]["option_1"],
            texts[selected_language]["option_2"],
            texts[selected_language]["option_3"],
            texts[selected_language]["option_4"],
            texts[selected_language]["option_5"]
        ]
        
        # Créer les boutons radio avec ttk pour un style amélioré
        style = ttk.Style()
        style.configure("TRadiobutton", font=("Helvetica", 12))  # Taille de police personnalisée

        for i, text in enumerate(options, start=1):
            radio_button = ttk.Radiobutton(frame_radio, text=text, variable=selected_value, value=i, style="TRadiobutton")
            radio_button.pack(side=tk.LEFT, padx=20)  # `side=tk.LEFT` pour alignement horizontal

        button_next = ttk.Button(root, text=texts[selected_language]["next_proposition"], command=lambda: next_proposition(selected_value), width=20)
        button_next.pack(side=tk.BOTTOM, pady=20)  # Bouton aligné en bas

    else:
        end_test()

# Enregistrer la réponse et passer à la proposition suivante
def next_proposition(selected_value):
    global current_proposition, responses
    response = selected_value.get()
    if response != 0:
        responses.append(response)
        print(f"Réponse enregistrée pour la proposition {current_proposition + 1}: {response}")
        current_proposition += 1
        show_proposition()
    else:
        label_warning = tk.Label(root, text=texts[selected_language]["select_option"], fg="red", pady=10, padx=20)
        label_warning.pack()

# Fin du test
def end_test():
    clear_window()

    label_end = tk.Label(root, text=texts[selected_language]["test_complete"], font=("Helvetica", 16), padx=20, pady=220)
    label_end.pack()

    button_report = ttk.Button(root, text=texts[selected_language]["show_report"], command=show_report, width=20)
    #button_report = ttk.Button(root, text="Afficher le rapport",  width=20)
    button_report.pack(side=tk.BOTTOM, pady=20)  # Bouton aligné en bas

#responses = [random.randint(3, 5) for _ in range(241)]

liste = list(range(1, 241))#liste de nombre de 1 a 240 

#liste de question a iterpretation dessendante 
dsd_indices =[0, 3, 6, 7, 9, 10, 13, 16, 17, 19, 20, 22, 26, 27, 29, 31, 32, 34, 35, 38,
 41, 42, 44, 45, 48, 51, 52, 54, 55, 58, 60, 63, 66, 67, 69, 70, 73, 76,
 77, 79, 80, 83, 86, 87, 89, 91, 92, 94, 95, 98, 101, 102, 104, 105, 108,
 111, 112, 114, 115, 118, 120, 123, 126, 127, 129, 133, 136, 137, 139, 140,
 143, 146, 147, 149, 152, 154, 155, 158, 161, 162, 165, 168, 172, 174, 175,
 180, 182, 186, 188, 189, 197, 198, 204, 205, 206, 207, 212, 218, 219, 221,
 227, 228, 230, 233, 235, 237]


    #creation d'une liste a interpretation assendante
asd_indices = [x for x in liste if x not in dsd_indices]

def traitement (responses,i):
    
    if i in asd_indices:
        if responses[i] == 1:
            return 0
        elif responses[i] == 2:
            return 1
        elif responses[i] == 3:
            return 2
        elif responses[i] == 4:
            return 3
        elif responses[i] == 5:
            return 4
        
    elif i in dsd_indices:
        if responses[i] == 1:
            return 4
        elif responses[i] == 2:
            return 3
        elif responses[i] == 3:
            return 2
        elif responses[i] == 4:
            return 1
        elif responses[i] == 5:
            return 0
        
    else:
        print(f"Erreur: l'indice {i} n'appartient ni dans asd ni dans dsd.")

def calcul():
  global N,N1,N2,N3,N4,N5,N6
  global E,E1,E2,E3,E4,E5,E6
  global O,O1,O2,O3,O4,O5,O6
  global A,A1,A2,A3,A4,A5,A6
  global C,C1,C2,C3,C4,C5,C6
  global TN,TN1,TN2,TN3,TN4,TN5,TN6
  global TE,TE1,TE2,TE3,TE4,TE5,TE6
  global TO,TO1,TO2,TO3,TO4,TO5,TO6
  global TA,TA1,TA2,TA3,TA4,TA5,TA6
  global TC,TC1,TC2,TC3,TC4,TC5,TC6
  global MD,SC,IC,AI,CC,OE,AG,EP
  global NEV,EXT,OUV,AGR,CON
  global text_N,text_E,text_O,text_A,text_C,text_MD,text_SC,text_IC,text_AI,text_CC,text_OE,text_AG,text_EP
  global text_TN1,text_TN2,text_TN3,text_TN4,text_TN5,text_TN6,text_TE1,text_TE2,text_TE3,text_TE4,text_TE5,text_TE6,text_TO1,text_TO2,text_TO3,text_TO4,text_TO5,text_TO6,text_TA1,text_TA2,text_TA3,text_TA4,text_TA5,text_TA6,text_TC1,text_TC2,text_TC3,text_TC4,text_TC5,text_TC6

  
    
  

  E1=int(traitement(responses,2-1))
  O1=int(traitement(responses,3-1))
  C1=int(traitement(responses,5-1))
  N2=int(traitement(responses,6-1))
  A2=int(traitement(responses,9-1))
  E3=int(traitement(responses,12-1))
  O3=int(traitement(responses,13-1))
  C3=int(traitement(responses,15-1))
  N4=int(traitement(responses,16-1))
  A4=int(traitement(responses,19-1))
  E5=int(traitement(responses,22-1))
  A5=int(traitement(responses,24-1))
  C5=int(traitement(responses,25-1))
  N6=int(traitement(responses,26-1))
  A6=int(traitement(responses,29-1))
  N7=int(traitement(responses,31-1))
  A7=int(traitement(responses,34-1))
  E8=int(traitement(responses,37-1))
  O8=int(traitement(responses,38-1))
  C8=int(traitement(responses,40-1))
  N9=int(traitement(responses,41-1))
  A9=int(traitement(responses,44-1))
  E10=int(traitement(responses,47-1))
  O10=int(traitement(responses,48-1))
  C10=int(traitement(responses,50-1))
  N11=int(traitement(responses,51-1))
  A11=int(traitement(responses,54-1))
  E12=int(traitement(responses,57-1))
  O12=int(traitement(responses,58-1))
  C12=int(traitement(responses,60-1))
  E13=int(traitement(responses,62-1))
  O13=int(traitement(responses,63-1))
  C13=int(traitement(responses,65-1))
  N14=int(traitement(responses,66-1))
  A14=int(traitement(responses,69-1))
  E15=int(traitement(responses,72-1))
  O15=int(traitement(responses,73-1))
  C15=int(traitement(responses,75-1))
  N16=int(traitement(responses,76-1))
  A16=int(traitement(responses,79-1))
  E17=int(traitement(responses,82-1))
  O17=int(traitement(responses,83-1))
  C17=int(traitement(responses,85-1))
  N18=int(traitement(responses,86-1))
  A18=int(traitement(responses,89-1))
  N19=int(traitement(responses,91-1))
  A19=int(traitement(responses,94-1))
  E20=int(traitement(responses,97-1))
  O20=int(traitement(responses,98-1))
  C20=int(traitement(responses,100-1))
  N21=int(traitement(responses,101-1))
  A21=int(traitement(responses,104-1))
  E22=int(traitement(responses,107-1))
  O22=int(traitement(responses,108-1))
  C22=int(traitement(responses,110-1))
  N23=int(traitement(responses,111-1))
  A23=int(traitement(responses,114-1))
  E24=int(traitement(responses,117-1))
  O24=int(traitement(responses,118-1))
  C24=int(traitement(responses,120-1))
  E25=int(traitement(responses,122-1))
  O25=int(traitement(responses,123-1))
  C25=int(traitement(responses,125-1))
  N26=int(traitement(responses,126-1))
  A26=int(traitement(responses,129-1))
  N27=int(traitement(responses,131-1))
  E27=int(traitement(responses,132-1))
  O27=int(traitement(responses,133-1))
  C27=int(traitement(responses,135-1))
  N28=int(traitement(responses,136-1))
  A28=int(traitement(responses,139-1))
  E29=int(traitement(responses,142-1))
  O29=int(traitement(responses,143-1))
  C29=int(traitement(responses,145-1))
  N30=int(traitement(responses,146-1))
  A30=int(traitement(responses,149-1))
  N31=int(traitement(responses,151-1))
  E31=int(traitement(responses,152-1))
  A31=int(traitement(responses,154-1))
  E32=int(traitement(responses,157-1))
  O32=int(traitement(responses,158-1))
  C32=int(traitement(responses,160-1))
  N33=int(traitement(responses,161-1))
  A33=int(traitement(responses,164-1))
  C33=int(traitement(responses,165-1))
  E34=int(traitement(responses,167-1))
  O34=int(traitement(responses,168-1))
  C34=int(traitement(responses,170-1))
  N35=int(traitement(responses,171-1))
  E35=int(traitement(responses,172-1))
  A35=int(traitement(responses,174-1))
  E36=int(traitement(responses,177-1))
  O36=int(traitement(responses,178-1))
  A36=int(traitement(responses,179-1))
  C36=int(traitement(responses,180-1))
  E37=int(traitement(responses,182-1))
  A37=int(traitement(responses,184-1))
  C37=int(traitement(responses,185-1))
  N38=int(traitement(responses,186-1))
  O38=int(traitement(responses,188-1))
  N39=int(traitement(responses,191-1))
  E39=int(traitement(responses,192-1))
  O39=int(traitement(responses,193-1))
  A39=int(traitement(responses,194-1))
  C39=int(traitement(responses,195-1))
  N40=int(traitement(responses,196-1))
  E40=int(traitement(responses,197-1))
  C40=int(traitement(responses,200-1))
  N41=int(traitement(responses,201-1))
  E41=int(traitement(responses,202-1))
  O41=int(traitement(responses,203-1))
  A41=int(traitement(responses,204-1))
  A42=int(traitement(responses,209-1))
  C42=int(traitement(responses,210-1))
  N43=int(traitement(responses,211-1))
  E43=int(traitement(responses,212-1))
  A43=int(traitement(responses,214-1))
  C43=int(traitement(responses,215-1))
  N44=int(traitement(responses,216-1))
  E44=int(traitement(responses,217-1))
  O44=int(traitement(responses,218-1))
  N45=int(traitement(responses,221-1))
  O45=int(traitement(responses,223-1))
  A45=int(traitement(responses,224-1))
  C45=int(traitement(responses,225-1))
  N46=int(traitement(responses,226-1))
  E46=int(traitement(responses,227-1))
  C46=int(traitement(responses,230-1))
  E47=int(traitement(responses,232-1))
  O47=int(traitement(responses,233-1))
  C47=int(traitement(responses,235-1))
  E48=int(traitement(responses,237-1))
  A48=int(traitement(responses,239-1))
  C48=int(traitement(responses,240-1))
  N1=int(traitement(responses,1-1))
  A1=int(traitement(responses,4-1))
  E2=int(traitement(responses,7-1))
  O2=int(traitement(responses,8-1))
  C2=int(traitement(responses,10-1))
  N3=int(traitement(responses,11-1))
  A3=int(traitement(responses,14-1))
  E4=int(traitement(responses,17-1))
  O4=int(traitement(responses,18-1))
  C4=int(traitement(responses,20-1))
  N5=int(traitement(responses,21-1))
  O5=int(traitement(responses,23-1))
  E6=int(traitement(responses,27-1))
  O6=int(traitement(responses,28-1))
  C6=int(traitement(responses,30-1))
  E7=int(traitement(responses,32-1))
  O7=int(traitement(responses,33-1))
  C7=int(traitement(responses,35-1))
  N8=int(traitement(responses,36-1))
  A8=int(traitement(responses,39-1))
  E9=int(traitement(responses,42-1))
  O9=int(traitement(responses,43-1))
  C9=int(traitement(responses,45-1))
  N10=int(traitement(responses,46-1))
  A10=int(traitement(responses,49-1))
  E11=int(traitement(responses,52-1))
  O11=int(traitement(responses,53-1))
  C11=int(traitement(responses,55-1))
  N12=int(traitement(responses,56-1))
  A12=int(traitement(responses,59-1))
  N13=int(traitement(responses,61-1))
  A13=int(traitement(responses,64-1))
  E14=int(traitement(responses,67-1))
  O14=int(traitement(responses,68-1))
  C14=int(traitement(responses,70-1))
  N15=int(traitement(responses,71-1))
  A15=int(traitement(responses,74-1))
  E16=int(traitement(responses,77-1))
  O16=int(traitement(responses,78-1))
  C16=int(traitement(responses,80-1))
  N17=int(traitement(responses,81-1))
  A17=int(traitement(responses,84-1))
  E18=int(traitement(responses,87-1))
  O18=int(traitement(responses,88-1))
  C18=int(traitement(responses,90-1))
  E19=int(traitement(responses,92-1))
  O19=int(traitement(responses,93-1))
  C19=int(traitement(responses,95-1))
  N20=int(traitement(responses,96-1))
  A20=int(traitement(responses,99-1))
  E21=int(traitement(responses,102-1))
  O21=int(traitement(responses,103-1))
  C21=int(traitement(responses,105-1))
  N22=int(traitement(responses,106-1))
  A22=int(traitement(responses,109-1))
  E23=int(traitement(responses,112-1))
  O23=int(traitement(responses,113-1))
  C23=int(traitement(responses,115-1))
  N24=int(traitement(responses,116-1))
  A24=int(traitement(responses,119-1))
  N25=int(traitement(responses,121-1))
  A25=int(traitement(responses,124-1))
  E26=int(traitement(responses,127-1))
  O26=int(traitement(responses,128-1))
  C26=int(traitement(responses,130-1))
  A27=int(traitement(responses,134-1))
  E28=int(traitement(responses,137-1))
  O28=int(traitement(responses,138-1))
  C28=int(traitement(responses,140-1))
  N29=int(traitement(responses,141-1))
  A29=int(traitement(responses,144-1))
  E30=int(traitement(responses,147-1))
  O30=int(traitement(responses,148-1))
  C30=int(traitement(responses,150-1))
  O31=int(traitement(responses,153-1))
  C31=int(traitement(responses,155-1))
  N32=int(traitement(responses,156-1))
  A32=int(traitement(responses,159-1))
  E33=int(traitement(responses,162-1))
  O33=int(traitement(responses,163-1))
  N34=int(traitement(responses,166-1))
  A34=int(traitement(responses,169-1))
  O35=int(traitement(responses,173-1))
  C35=int(traitement(responses,175-1))
  N36=int(traitement(responses,176-1))
  N37=int(traitement(responses,181-1))
  O37=int(traitement(responses,183-1))
  E38=int(traitement(responses,187-1))
  A38=int(traitement(responses,189-1))
  C38=int(traitement(responses,190-1))
  O40=int(traitement(responses,198-1))
  A40=int(traitement(responses,199-1))
  C41=int(traitement(responses,205-1))
  N42=int(traitement(responses,206-1))
  E42=int(traitement(responses,207-1))
  O42=int(traitement(responses,208-1))
  O43=int(traitement(responses,213-1))
  A44=int(traitement(responses,219-1))
  C44=int(traitement(responses,220-1))
  E45=int(traitement(responses,222-1))
  O46=int(traitement(responses,228-1))
  A46=int(traitement(responses,229-1))
  N47=int(traitement(responses,231-1))
  A47=int(traitement(responses,234-1))
  N48=int(traitement(responses,236-1))
  O48=int(traitement(responses,238-1))
  print(N1,N2,N3,N4,N5,N6)
  #calcule des indices de N
  N1=N1+N7+N13+N19+N25+N31+N37+N43
  N2=N2+N8+N14+N20+N26+N32+N38+N44
  N3=N3+N9+N15+N21+N27+N33+N39+N45
  N4=N4+N10+N16+N22+N28+N34+N40+N46
  N5=N5+N11+N17+N23+N29+N35+N41+N47
  N6=N6+N12+N18+N24+N30+N36+N42+N48
  N=N1+N2+N3+N4+N5+N6
  print(N1,N2,N3,N4,N5,N6)
  print(N)

  #calcule des indices de E
  E1=E1+E7+E13+E19+E25+E31+E37+E43
  E2=E2+E8+E14+E20+E26+E32+E38+E44
  E3=E3+E9+E15+E21+E27+E33+E39+E45
  E4=E4+E10+E16+E22+E28+E34+E40+E46
  E5=E5+E11+E17+E23+E29+E35+E41+E47
  E6=E6+E12+E18+E24+E30+E36+E42+E48
  E=E1+E2+E3+E4+E5+E6
  print(E1,E2,E3,E4,E5,E6)
  print(E)

  #calcule des indices de O
  O1=O1+O7+O13+O19+O25+O31+O37+O43
  O2=O2+O8+O14+O20+O26+O32+O38+O44
  O3=O3+O9+O15+O21+O27+O33+O39+O45
  O4=O4+O10+O16+O22+O28+O34+O40+O46
  O5=O5+O11+O17+O23+O29+O35+O41+O47
  O6=O6+O12+O18+O24+O30+O36+O42+O48
  O=O1+O2+O3+O4+O5+O6
  print(O1,O2,O3,O4,O5,O6)
  print(O)

  #calcule des indices de A
  A1=A1+A7+A13+A19+A25+A31+A37+A43
  A2=A2+A8+A14+A20+A26+A32+A38+A44
  A3=A3+A9+A15+A21+A27+A33+A39+A45
  A4=A4+A10+A16+A22+A28+A34+A40+A46
  A5=A5+A11+A17+A23+A29+A35+A41+A47
  A6=A6+A12+A18+A24+A30+A36+A42+A48
  A=A1+A2+A3+A4+A5+A6
  print(A1,A2,A3,A4,A5,A6)
  print(A)

  #calcule des indices de C
  C1=C1+C7+C13+C19+C25+C31+C37+C43
  C2=C2+C8+C14+C20+C26+C32+C38+C44
  C3=C3+C9+C15+C21+C27+C33+C39+C45
  C4=C4+C10+C16+C22+C28+C34+C40+C46
  C5=C5+C11+C17+C23+C29+C35+C41+C47
  C6=C6+C12+C18+C24+C30+C36+C42+C48
  C=C1+C2+C3+C4+C5+C6
  print(C1,C2,C3,C4,C5,C6)
  print(C)



  TN1 =int(TNOTE.clacule_noteT_N1(sexe.get(),N1))
  TN2 =int(TNOTE.clacule_noteT_N2(sexe.get(),N2))
  TN3 =int(TNOTE.clacule_noteT_N3(sexe.get(),N3))
  TN4 =int(TNOTE.clacule_noteT_N4(sexe.get(),N4))
  TN5 =int(TNOTE.clacule_noteT_N5(sexe.get(),N5))
  TN6 =int(TNOTE.clacule_noteT_N6(sexe.get(),N6))
  TE1 =int(TNOTE.clacule_noteT_E1(sexe.get(),E1))
  TE2 =int(TNOTE.clacule_noteT_E2(sexe.get(),E2))
  TE3 =int(TNOTE.clacule_noteT_E3(sexe.get(),E3)) 
  TE4 =int(TNOTE.clacule_noteT_E4(sexe.get(),E4))
  TE5 =int(TNOTE.clacule_noteT_E5(sexe.get(),E5))
  TE6 =int(TNOTE.clacule_noteT_E6(sexe.get(),E6))
  TO1 =int(TNOTE.clacule_noteT_O1(sexe.get(),O1))
  TO2 =int(TNOTE.clacule_noteT_O2(sexe.get(),O2))
  TO3 =int(TNOTE.clacule_noteT_O3(sexe.get(),O3))
  TO4 =int(TNOTE.clacule_noteT_O4(sexe.get(),O4))
  TO5 =int(TNOTE.clacule_noteT_O5(sexe.get(),O5))
  TO6 =int(TNOTE.clacule_noteT_O6(sexe.get(),O6))
  TA1 =int(TNOTE.clacule_noteT_A1(sexe.get(),A1))
  TA2 =int(TNOTE.clacule_noteT_A2(sexe.get(),A2))
  TA3 =int(TNOTE.clacule_noteT_A3(sexe.get(),A3))
  TA4 =int(TNOTE.clacule_noteT_A4(sexe.get(),A4))
  TA5 =int(TNOTE.clacule_noteT_A5(sexe.get(),A5))
  TA6 =int(TNOTE.clacule_noteT_A6(sexe.get(),A6))
  TC1 =int(TNOTE.clacule_noteT_C1(sexe.get(),C1))
  TC2 =int(TNOTE.clacule_noteT_C2(sexe.get(),C2))
  TC3 =int(TNOTE.clacule_noteT_C3(sexe.get(),C3))
  TC4 =int(TNOTE.clacule_noteT_C4(sexe.get(),C4))
  TC5 =int(TNOTE.clacule_noteT_C5(sexe.get(),C5))
  TC6 =int(TNOTE.clacule_noteT_C6(sexe.get(),C6))
  #print(TC1,TC2,TC3,TC4,TC5,TC6)
  #print(TN1,TN2,TN3,TN4,TN5,TN6)
  #print(TE1,TE2,TE3,TE4,TE5,TE6)
  #print(TO1,TO2,TO3,TO4,TO5,TO6)
  #print(TA1,TA2,TA3,TA4,TA5,TA6)  


  #variables = [
  #    TN1, TN2, TN3, TN4, TN5, TN6,
  #    TE1, TE2, TE3, TE4, TE5, TE6,
  #    TO1, TO2, TO3, TO4, TO5, TO6,
  #    TA1, TA2, TA3, TA4, TA5, TA6,
  #    TC1, TC2, TC3, TC4, TC5, TC6,
  #]

  #for i, value in enumerate(variables, start=1):
  #        if value < 20 or value > 80:
  #          print ("erreur lors du calcule des notes T")

  # Dictionnaire qui associe les intervalles de N à la note T correspondante


  # calcule des 5 grand trait 
  #N
  if(sexe.get()=="F"):
    NEV=TNOTE.FCORRESPONDANCE_NT(N)
  elif (sexe.get()=="H"):
    NEV=TNOTE.HCORRESPONDANCE_NT(N)
  else :
    NEV=-1
    print("erreur lors de l'interpretation du sexe du condidat")

  #E
  if(sexe.get()=="F"):
    EXT=TNOTE.FCORRESPONDANCE_ET(E)
  elif (sexe.get()=="H"):
    EXT=TNOTE.HCORRESPONDANCE_ET(E)
  else :
    print("erreur lors de l'interpretation du sexe du condidat")

  #O
  if(sexe.get()=="F"):
    OUV=TNOTE.FCORRESPONDANCE_OT(O)
  elif (sexe.get()=="H"):
    OUV=TNOTE.HCORRESPONDANCE_OT(O)
  else :
    print("erreur lors de l'interpretation du sexe du condidat")

  #A 
  if(sexe.get()=="F"):
    AGR=TNOTE.FCORRESPONDANCE_AT(A)
  elif (sexe.get()=="H"):
    AGR=TNOTE.HCORRESPONDANCE_AT(A)
  else :
    print("erreur lors de l'interpretation du sexe du condidat")

  #C
  if(sexe.get()=="F"):
    CON=TNOTE.FCORRESPONDANCE_CT(C)
  elif (sexe.get()=="H"):
    CON=TNOTE.HCORRESPONDANCE_CT(C)
  else :
    print("erreur lors de l'interpretation du sexe du condidat")

  MD=round((TE3+TN2+TC4)/3, 2) #mener et decider
  SC=round((TA3+TA1+TE1)/3, 2) #soutnir et cooperer
  IC=round((TA3+TA1+TE1)/3, 2) #interagire et communiquer
  AI=round((TC6+TC1+TO5)/3, 2) #Analyser et interpreter
  CC=round((TE4+TO2+TE5)/3, 2) #creer et conceptualiser
  OE=round((TC2+TC5+TA4)/3, 2) #organiser et executer
  AG=round((TN1+TN6+TC3)/3, 2) #s'adapter et gerer la pression 
  EP=round((TN5+TE4+TC4)/3, 2) #entreprendre et performr

  #print(NEV,EXT,OUV,AGR,CON )
  #print("\n")
  #print("MD",MD,"SC",SC,"IC",IC,"AI",AI,"CC",CC,"OE",OE,"AG",AG,"EP",EP)
#

  text_TN1=text_TN2=text_TN3=text_TN4=text_TN5=text_TN6=text_TE1=text_TE2=text_TE3=text_TE4=text_TE5=text_TE6=text_TO1=text_TO2=text_TO3=text_TO4=text_TO5=text_TO6=text_TA1=text_TA2=text_TA3=text_TA4=text_TA5=text_TA6=text_TC1=text_TC2=text_TC3=text_TC4=text_TC5=text_TC6="Cette persson est dans la Norme"
  text_N="Erreur lors du calcule du coeficient de nevrosite"
  text_A="Erreur lors du calcule du coeficient de AGREABILITE"
  text_E="Erreur lors du calcule du coeficient de EXTRAVERSSION"
  text_O="Erreur lors du calcule du coeficient de OUVERTURE"
  text_C="Erreur lors du calcule du coeficient de CONSIENCE"
  text_AG=text_AI=text_CC=text_EP=text_IC=text_MD=text_OE=text_SC="Erreur de calcule  "


  #anxiete
  if TN1 >= 56 :
    text_TN1="auront plus tendance à éprouver de telles peurs et à souffrir d ’anxiété diffuse nerveux"
  elif   43<= TN1 <=20 :
    text_TN1="sont, en revanche, calmes et détendues"
  #colere
  if TN2 >= 56 :
      text_TN2="facile à se mettre en colère"
  elif   43<= TN2 >=20 :
    text_TN2="il ce mes on colère difficilement"
  #depression
  if TN3 >= 56 :
    text_TN3="sont sujettes à la culpabilité, à la tristesse, à des sentiments d ’impuissance et de solitude. Elles sont facilement découragées et souvent abattues"
  elif   43<= TN3 >=20 :
    text_TN3="éprouvent, en revanche, rarement de telles émotions mais elles ne sont pas nécessairement gaies et enjouées, ces caractéristiques étant liées à l ’extraversion"
  #timidite sociale
  if TN4 >= 56 :
    text_TN4="Les individus timides en société sont mal à l ’aise en présence des autres, sensibles au ridicule et ont tendance à se sentir inférieurs.  La timidité sociale se rapproche de l ’anxiété sociale-en ce qui concerne la timidité sociale en public"
  elif   43<= TN4 >=20 :
    text_TN4="Elles sont simplement moins perturbées par les situations sociales embarrassantes"
  #impulsivite
  if TN5 >= 56 :
    text_TN5="l ’incapacité à maîtriser ses désirs et ses besoins"
  elif   43<= TN5 >=20 :
    text_TN5="plus de facilité à résister à de telles tentations parce qu ’elles tolèrent mieux la frustration"
  #vulnerabilite
  if TN6 >= 56 :
    text_TN6="incapables de faire face au stress"
  elif   43<= TN6 >=20 :
    text_TN6="capables de se contrôler dans les situations difficiles"

  #chaleur
  if TE1 >= 56 :
    text_TE1="personnes chaleureuses sont affectueuses et amicales nouent facilement des relations proches avec les autres"
  elif   43<= TE1 >=20 :
    text_TE1="elles sont plus formalistes, plus réservées et distantes"
  #gregarite
  if TE2 >= 56 :
      text_TE2="Les personnes grégaires apprécient la compagnie d ’autrui"
  elif   43<= TE2 >=20 :
    text_TE2="sont plutôt des solitaires qui ne recherchent pas - ou qui évitent même activement - les stimulations sociales"
  #assertivite
  if TE3 >= 56 :
    text_TE3="ont tendance à se montrer dominantes, énergiques et ambitieuses socialement"
  elif   43<= TE3 >=20 :
    text_TE3="préfèrent, en revanche, se tenir à l ’écart et laisser les autres parler"
  #activite
  if TE4 >= 56 :
    text_TE4="personnes ayant un rythme rapide. Elles sont vigoureuses, énergiques et ont besoin d ’être constamment occupées"
  elif   43<= TE4 >=20 :
    text_TE4="quant à elles, un tempo plus lent et plus tranquille même si elles ne sont pas nécessairement apathiques ou paresseuses"
  #recherche sensation
  if TE5 >= 56 :
    text_TE5="éprouvent un besoin impérieux d ’animation et de stimulation. Elles apprécient les couleurs vives et les environnements bruyants"
  elif   43<= TE5 >=20 :
    text_TE5="n ’éprouvent, en revanche, pas beaucoup ce besoin de stimulation et mènent une vie que les précédentes pourraient trouver ennuyeuse"
  #emotion positive
  if TE6 >= 56 :
    text_TE6="cette échelle rient facilement et souvent. Elles sont gaies et optimistes"
  elif   43<= TE6 >=20 :
    text_TE6="Elles sont simplement moins exubérantes et moins vives"

  #reveries
  if TO1 >= 56 :
    text_TO1="Elles élaborent et développent leur imaginaire et pensent que l ’imagination procure une vie riche et créative"
  elif   43<= TO1 >=20 :
    text_TO1="sont plus prosaïques et préfèrent s ’en tenir à ce qu ’elles font"
  #esthetique
  if TO2 >= 56 :
      text_TO2="apprécient l ’art et la beauté"
  elif   43<= TO2 >=20 :
    text_TO2="sont, en revanche, insensibles à l ’art et à la beauté ou s ’y intéressent peu"
  #sentiments
  if TO3 >= 56 :
    text_TO3=" éprouvent une gamme d ’états émotionnels différents plus large et les vivent plus profondément"
  elif   43<= TO3 >=20 :
    text_TO3=" n ’accordent pas d ’importance aux états émotionnels et leurs affects semblent émoussées"
  #action
  if TO4 >= 56 :
    text_TO4="peuvent au cours du temps se lancer dans une série d ’activités de loisirs différentes"
  elif   43<= TO4 >=20 :
    text_TO4="trouvent le changement difficile et préfèrent s’en tenir à ce qu’elles connaissent et apprécient déjà"
  #idee
  if TO5 >= 56 :
    text_TO5="une ouverture d ’esprit aux idées nouvelles et parfois non conventionnelles"
  elif   43<= TO5 >=20 :
    text_TO5=" il n'accept pas des nouvelles idées"
  #valeur
  if TO6 >= 56 :
    text_TO6="L ’ouverture aux valeurs est la disposition à remettre en question les valeurs sociales, politiques et religieuses"
  elif   43<= TO6 >=20 :
    text_TO6="les individus fermés ont tendance à accepter l ’autorité et à respecter les traditions"
  #confience
  if TA1 >= 56 :
    text_TA1="ont tendance à penser que les autres sont honnêtes et bien intentionnés"
  elif   43<= TA1 >=20 :
    text_TA1="ont tendance à se montrer cyniques et sceptiques et à partir du principe que les autres peuvent être malhonnêtes ou dangereux"
  #droiture
  if TA2 >= 56 :
      text_TA2="sont franches et sincères"
  elif   43<= TA2 >=20 :
    text_TA2="cette personne est malhonnête ou manipulatrice"
  #altruisme
  if TA3 >= 56 :
    text_TA3="pérsonne génireux et leur volonté d ’aider ceux qui en ont besoin"
  elif   43<= TA3 >=20 :
    text_TA3="plus centrées sur elles-mêmes et peu enclines à s ’impliquer dans les problèmes d ’autrui"
  #compliance
  if TA4 >= 56 :
    text_TA4="des personne humbles et douces"
  elif   43<= TA4 >=20 :
    text_TA4="sont agressives, préfèrent la compétition à la coopération et n ’hésitent pas à exprimer leur colère quand c ’est nécessaire"
  #modestie
  if TA5 >= 56 :
    text_TA5="sont humbles et s ’effacent, bien qu’elles ne manquent pas toujours de confiance en elles ou d ’estime de soi"
  elif   43<= TA5 >=20 :
    text_TA5="ont une image positive d ’elles-mêmes et peuvent être perçues comme arrogantes et prétentieuses par les autres. Un « manque pathologique » de modestie fait partie de la conception clinique du narcissisme"
  #sensibilite
  if TA6 >= 56 :
    text_TA6="sont touchés par les besoins d ’autrui et mettent l ’accent sur l ’aspect humain de la politique sociale"
  elif   43<= TA6 >=20 :
    text_TA6="sont plus durs et moins émus par les appels à la pitié. Ils se considèrent comme des réalistes qui prennent des décisions rationnelles fondées sur une logique froide"
  #competance
  if TC1 >= 56 :
    text_TC1="se sentent bien préparées pour affronter la vie"
  elif   43<= TC1 >=20 :
    text_TC1="ont, en revanche, une piètre opinion de leurs capacités"
  #ordre
  if TC2 >= 56 :
      text_TC2="sont bien organisées, ordonnées et soignées"
  elif   43<= TC2 >=20 :
    text_TC2="sont incapables de s ’organiser et se décrivent comme manquant de méthode"
  #sens du devoir
  if TC3 >= 56 :
    text_TC3="adhèrent strictement à leurs principes éthiques et remplissent scrupuleusement leurs obligations morales"
  elif   43<= TC3 >=20 :
    text_TC3="sont plus désinvoltes et peuvent se montrer peu fiables ou instables"
  #recherche reussite
  if TC4 >= 56 :
    text_TC4="peuvent cependant trop s ’investir dans leur carrière et devenir des bourreaux de travail"
  elif   43<= TC4 >=20 :
    text_TC4="Elles ne « s ’accrochent pas » assez pour réussir. Elles manquent d ’ambition et peuvent donner l ’impression de n ’avoir aucun but dans l ’existence car elles se satisfont souvent de leur faible niveau de réussite"
  #autodiscipline
  if TC5 >= 56 :
    text_TC5="ont la faculté de se motiver pour mener à bien ce qu’il y a à faire"
  elif   43<= TC5 >=20 :
    text_TC5="ont, en revanche, tendance à remettre les corvées à plus tard et se montrent facilement découragées et désireuses de tout abandonner"
  #deliberation
  if TC6 >= 56 :
    text_TC6="sont prudentes et réfléchies"
  elif   43<= TC6 >=20 :
    text_TC6="sont précipitées. Elles parlent et agissent souvent sans envisager les conséquences de leurs paroles et de leurs actes. Dans le meilleur cas, elles sont spontanées et capables de prendre rapidement des décisions quand c ’est nécessaire"

  
  #Nevrosite
  #tres faible
  if( 20<=NEV<=33) :
    text_N="La personne présente une bonne régulation émotionnelle, fait preuve de sérénité, de confiance en soi et d'une capacité à gérer efficacement le stress et les émotions négatives."

  #faible
  elif(34<=NEV<=44):
    text_N="La personne présente une bonne régulation émotionnelle, fait preuve de sérénité, de confiance en soi et d'une capacité à gérer efficacement le stress et les émotions négatives."

  #moyen
  elif(45<=NEV<=55):
    text_N=": La personne démontre une capacité de gestion du stress qui se situe globalement dans la moyenne."

  #eleve
  elif(56<=NEV<=64):
    text_N="La personne manifeste une tendance à ressentir plus fréquemment des émotions négatives telles que la peur, la colère ou la tristesse, et peut rencontrer des difficultés à maîtriser ses réactions émotionnelles ainsi qu'à gérer efficacement le stress dans certaines situations."

  #tres eleve
  elif(65<=NEV<=80):
    text_N="La personne manifeste une tendance à ressentir plus fréquemment des émotions négatives telles que la peur, la colère ou la tristesse, et peut rencontrer des difficultés à maîtriser ses réactions émotionnelles ainsi qu'à gérer efficacement le stress dans certaines situations."


  #extraverssion
  #tres faible
  if( 20<=EXT<=33) :
    text_E="La personne présente un profil plutôt introverti, adoptant une attitude réservée sans pour autant être fermée aux autres. Elle se montre indépendante dans ses interactions sociales et fait preuve de constance dans son comportement. Cette tendance à l’introversion ne traduit ni isolement ni pessimisme, mais reflète une préférence pour la discrétion et les environnements calmes, sans lien nécessaire avec une anxiété sociale."

  #faible
  elif(34<=EXT<=44):
    text_E="La personne présente un profil plutôt introverti, adoptant une attitude réservée sans pour autant être fermée aux autres. Elle se montre indépendante dans ses interactions sociales et fait preuve de constance dans son comportement. Cette tendance à l’introversion ne traduit ni isolement ni pessimisme, mais reflète une préférence pour la discrétion et les environnements calmes, sans lien nécessaire avec une anxiété sociale."

  #moyen
  elif(45<=EXT<=55):
    text_E="La personne adopte un comportement généralement équilibré sur le plan de l’extraversion, en manifestant une sociabilité, une assertivité, un dynamisme et un optimisme qui s’inscrivent globalement dans la moyenne."

  #eleve
  elif(56<=EXT<=64):
    text_E="La personne présente un profil extraverti, marqué par une aisance en société et une préférence pour les interactions en groupe. Elle se distingue par une attitude dynamique, communicative et confiante, appréciant les environnements stimulants et faisant preuve d’enthousiasme, d’énergie et d’optimisme."

  #tres eleve
  elif(65<=EXT<=80):
    text_E="La personne présente un profil extraverti, marqué par une aisance en société et une préférence pour les interactions en groupe. Elle se distingue par une attitude dynamique, communicative et confiante, appréciant les environnements stimulants et faisant preuve d’enthousiasme, d’énergie et d’optimisme."

  #ouverture
  #tres faible
  if( 20<=OUV<=33) :
    text_O="La personne évaluée présente généralement une tendance à adopter des idées et des comportements de nature conservatrice et conventionnelle. Elle manifeste une préférence pour les situations familières plutôt que pour la nouveauté, avec des réactions émotionnelles généralement modérées. Ce profil semble également se caractériser par des centres d’intérêt relativement restreints et d’intensité modérée."

  #faible
  elif(34<=OUV<=44):
    text_O="La personne évaluée présente généralement une tendance à adopter des idées et des comportements de nature conservatrice et conventionnelle. Elle manifeste une préférence pour les situations familières plutôt que pour la nouveauté, avec des réactions émotionnelles généralement modérées. Ce profil semble également se caractériser par des centres d’intérêt relativement restreints et d’intensité modérée."

  #moyenne
  elif(45<=OUV<=55):
    text_O="Le profil évalué reflète une ouverture modérée aux idées nouvelles, faisant preuve d’un niveau moyen de curiosité intellectuelle, d’imagination, de créativité, d’introspection et de sensibilité artistique."

  #eleve
  elif(56<=OUV<=64):
    text_O="La personne évaluée présente un score élevé sur la dimension de l’ouverture. Ce profil se caractérise par une imagination vive, une sensibilité esthétique marquée, une attention portée à l’univers intérieur, une curiosité intellectuelle, une préférence pour la diversité, ainsi qu’une indépendance dans les jugements. Les individus ayant ce type de profil sont généralement réceptifs aux idées nouvelles, ouverts à des valeurs non conventionnelles, et recherchent des expériences variées. Ils/elles ont également tendance à vivre les émotions, qu’elles soient positives ou négatives, de manière plus intense que les personnes plus réservées."

  #tres eleve
  elif(65<=OUV<=80):
    text_O="La personne évaluée présente un score élevé sur la dimension de l’ouverture. Ce profil se caractérise par une imagination vive, une sensibilité esthétique marquée, une attention portée à l’univers intérieur, une curiosité intellectuelle, une préférence pour la diversité, ainsi qu’une indépendance dans les jugements. Les individus ayant ce type de profil sont généralement réceptifs aux idées nouvelles, ouverts à des valeurs non conventionnelles, et recherchent des expériences variées. Ils/elles ont également tendance à vivre les émotions, qu’elles soient positives ou négatives, de manière plus intense que les personnes plus réservées."

  #agreabilite
  #tres faible
  if( 20<=AGR<=33) :
    text_A="La personne évaluée peut parfois être perçue comme distante ou peu conciliante dans ses relations interpersonnelles. Ce profil peut refléter une tendance à privilégier ses propres besoins, avec une propension à adopter des attitudes marquées par une certaine méfiance ou un manque de flexibilité sociale."

  #faible
  elif(34<=AGR<=44):
    text_A="La personne évaluée peut parfois être perçue comme distante ou peu conciliante dans ses relations interpersonnelles. Ce profil peut refléter une tendance à privilégier ses propres besoins, avec une propension à adopter des attitudes marquées par une certaine méfiance ou un manque de flexibilité sociale."

  #moyen
  elif(45<=AGR<=55):
    text_A="La personne évaluée adopte généralement une posture équilibrée dans ses relations interpersonnelles. Elle se distingue par sa franchise et sa sincérité, et prend ses décisions de manière réfléchie, en s’appuyant sur une logique claire et rationnelle."

  #elve 
  elif(56<=AGR<=64):
    text_A="La personne évaluée présente une disposition marquée à l’altruisme. Elle manifeste de l’empathie envers autrui, se montre volontaire pour apporter son aide, et adopte une attitude généralement confiante quant à la réciprocité dans les relations humaines."

  #eleve
  elif(65<=AGR<=80):
    text_A="La personne évaluée présente une disposition marquée à l’altruisme. Elle manifeste de l’empathie envers autrui, se montre volontaire pour apporter son aide, et adopte une attitude généralement confiante quant à la réciprocité dans les relations humaines."

  #CONSCIENCE
  #tres faible
  if( 20<=CON<=33):
    text_C="La personne évaluée peut faire preuve d’une certaine souplesse dans l’application de principes ou de normes, et adopter une approche moins rigide dans la poursuite de ses objectifs."

  #faible
  elif(34<=CON<=44):
    text_C="La personne évaluée peut faire preuve d’une certaine souplesse dans l’application de principes ou de normes, et adopter une approche moins rigide dans la poursuite de ses objectifs."

  #moyen
  elif(45<=CON<=55):
    text_C="La personne évaluée présente un niveau d’implication modéré dans les activités de planification, d’organisation et de mise en œuvre des tâches."
  
  #eleve
  elif(56<=CON<=64):
    text_C="La personne évaluée démontre une implication notable dans la planification, l’organisation et l’exécution des tâches. Ce niveau de conscience élevé constitue généralement un atout favorable à la réussite professionnelle."

  #tres eleve
  elif(65<=CON<=80):
    text_C="La personne évaluée démontre une implication notable dans la planification, l’organisation et l’exécution des tâches. Ce niveau de conscience élevé constitue généralement un atout favorable à la réussite professionnelle."



  #menner et decider
  #faible
  if( 20<=MD<=44.99) :
    text_MD="La personne évaluée manifeste une tendance moins marquée à prendre l’initiative, à diriger ou à encadrer dans le cadre d’un projet ou d’une situation. Elle semble également adopter une posture plus réservée lorsqu’il s’agit d’assumer des responsabilités ou de formuler des directives."

  #moyen
  elif(45<=MD<=55.99):
    text_MD="La personne évaluée présente une capacité modérée à exercer un rôle de leadership, à initier des actions, à orienter un projet ou une situation, à formuler des directives et à assumer des responsabilités."

  #eleve
  elif(56<=MD<=80):
    text_MD="La personne évaluée semble disposer d’une bonne capacité à exercer un rôle de leadership, à prendre l’initiative, à orienter l’action, à encadrer les autres et à assumer des responsabilités dans le cadre de projets ou de situations variées."

  #soutnir et cooperer
  #faible
  if( 20<=SC<=44.99) :
    text_SC="La personne évaluée adopte une approche des relations de travail orientée vers l’autonomie et la performance individuelle, tout en restant ouverte à la collaboration lorsque cela est nécessaire. Elle accorde de l’importance au mérite et n’hésite pas à exprimer ses points de vue de manière directe, notamment en cas de désaccord."

  #moyen
  elif(45<=SC<=55.99):
    text_SC="La personne évaluée adopte une attitude généralement positive et respectueuse dans ses interactions avec les collègues, les supérieurs et les clients, particulièrement lorsque ces attitudes sont partagées. Elle se montre disposée à apporter son soutien au sein de l’équipe, mais peut-être moins encline à la collaboration ou à la participation collective si l’environnement de travail ne reflète pas ces mêmes valeurs."

  #eleve
  elif(56<=SC<=80):
    text_SC="La personne évaluée fait preuve d’une forte disposition à la collaboration et au soutien, en se montrant volontiers disponible pour aider autrui et contribuer activement au travail d’équipe en vue d’atteindre des objectifs partagés."



  #interagire et cooperer
  #faible
  if( 20<=IC<=44.99) :
    text_IC="La personne évaluée semble moins à l’aise dans les interactions sociales, notamment lorsqu’il s’agit d’établir de nouveaux contacts, de s’exprimer en groupe ou de défendre ses idées. Elle peut éprouver des difficultés à s’intégrer spontanément dans un collectif et à adopter une posture d’influence ou de persuasion."

  #moyen
  elif(45<=IC<=55.99):
    text_IC="La personne évaluée présente une aisance relationnelle modérée, avec une capacité moyenne à établir des contacts, à développer son réseau et à exercer de l’influence. Son niveau de confiance en soi se situe globalement dans la moyenne lorsqu’il s’agit d’interagir en groupe, de communiquer ses idées et de défendre son point de vue."

  #eleve
  elif(56<=IC<=80):
    text_IC="La personne évaluée dispose d’une forte aisance relationnelle, lui permettant de créer et d’entretenir un réseau de contacts, ainsi que d’exercer une influence positive et de convaincre. Elle fait preuve d’une confiance marquée dans les interactions sociales, que ce soit pour rencontrer de nouvelles personnes, s’exprimer en groupe ou défendre son point de vue."

  #analyser et interpreter
  #faible
  if( 20<=AI<=44.99) :
    text_AI="La personne évaluée manifeste une préférence pour les tâches concrètes et familières, et peut se montrer moins à l’aise face à des situations complexes nécessitant une analyse approfondie. Elle semble également plus encline à adopter des approches éprouvées, avec une certaine réserve vis-à-vis des changements ou des évolutions technologiques."

  #moyen
  elif(45<=AI<=55.99):
    text_AI="La personne évaluée présente un niveau moyen de pensée analytique et de confort dans le traitement de problématiques ou d’idées complexes. Son ouverture à la nouveauté, notamment aux évolutions technologiques, ainsi que sa capacité d’adaptation, se situent également dans la moyenne."

  #eleve
  elif(56<=AI<=80):
    text_AI="La personne évaluée montre une préférence pour les tâches complexes impliquant une analyse approfondie, plutôt que pour des activités routinières. Elle fait également preuve d’une bonne capacité d’adaptation face à la nouveauté, notamment en ce qui concerne les évolutions technologiques."


  #creer et conceptualiser
  #faible
  if( 20<=CC<=44.99) :
    text_CC="La personne évaluée montre une préférence pour les tâches concrètes et les environnements familiers, et s’appuie davantage sur des approches connues que sur l’exploration de nouvelles idées. Elle peut faire preuve de réserve face aux changements organisationnels et adopte une posture plus prudente lorsqu’il s’agit d’initier des transformations."

  #moyen
  elif(45<=CC<=55.99):
    text_CC="La personne évaluée présente une capacité moyenne en matière de conceptualisation et de création. Son approche est principalement orientée vers le pragmatisme, avec une préférence pour les solutions concrètes plutôt que pour les approches innovantes."

  #eleve
  elif(56<=CC<=80):
    text_CC="La personne évaluée est susceptible de bien réussir dans des contextes demandant ouverture aux idées nouvelles et aux expériences variées. Elle peut faire preuve d’innovation et de créativité dans la résolution de problèmes, tout en adoptant une attitude proactive face aux opportunités d’apprentissage et de développement. Réceptive au changement, elle est également en mesure de contribuer activement à sa mise en œuvre au sein de l’organisation."

  #organiser et executer
  #faible
  if( 20<=OE<=44.99) :
    text_OE="La personne évaluée pourrait rencontrer certains défis en matière d’organisation et d’exécution, et gagnerait à bénéficier d’un accompagnement ou d’opportunités de développement pour renforcer ses compétences dans ces domaines."

  #moyen
  elif(45<=OE<=55.99):
    text_OE="La personne évaluée adopte généralement une approche équilibrée en matière de planification, d’organisation du travail et de respect des consignes et procédures. Son fonctionnement reflète une rigueur modérée, sans excès de rigidité ni manque de structure."

  #eleve
  elif(56<=OE<=80):
    text_OE="La personne évaluée fait preuve d’efficacité dans la gestion du temps, avec une bonne capacité à hiérarchiser les priorités et à mener les projets à terme. Elle se distingue par sa fiabilité, le respect des délais, ainsi qu’une approche méthodique qui lui permet de gérer de manière organisée les différentes responsabilités qui lui sont confiées."

  #s'adapter et gerer la pression
  #faible 
  if( 20<=AG<=44.99) :
    text_AG="La personne évaluée peut rencontrer certaines limites dans sa capacité à gérer la pression, à s’adapter aux changements ou à faire face aux situations d’échec. Un accompagnement ciblé pourrait contribuer à renforcer ses compétences en matière de gestion du stress et d’adaptation."

  #moyen
  elif(45<=AG<=55.99):
    text_AG="La personne évaluée fait preuve d’une aptitude modérée à gérer la pression et à s’adapter aux imprévus ou aux échecs. Dans certaines circonstances, elle peut néanmoins éprouver un sentiment de dépassement face à la situation."

  #eleve
  elif(56<=AG<=80):
    text_AG="La personne évaluée fait preuve d’une bonne stabilité émotionnelle face aux situations stressantes. Elle s’adapte efficacement aux changements et parvient généralement à surmonter les obstacles sans se laisser déstabiliser."

  #entreprendre et performer
  #faible
  if( 20<=EP<=44.99) :
    text_EP="La personne évaluée semble faire face à quelques défis en matière de prise d’initiative et de performance. Un soutien adapté pourrait contribuer à renforcer ses compétences dans ces domaines ainsi qu’à développer davantage sa confiance en ses capacités."

  #moyen
  elif(45<=EP<=55.99):
    text_EP="La personne évaluée adopte une posture équilibrée vis-à-vis des objectifs et des résultats. Sans faire preuve de négligence ou de désengagement, elle ne se distingue pas particulièrement par une recherche active de performance ou de réussite. Les opportunités de développement et d’évolution professionnelle peuvent être perçues positivement, bien qu’elles ne constituent pas nécessairement une priorité centrale pour elle."

  #eleve
  elif(56<=EP<=80):
    text_EP="La personne évaluée ne présente pas de points de vigilance particuliers ni de domaines nécessitant une amélioration spécifique. Son profil reflète des caractéristiques de personnalité généralement associées à une bonne capacité d’initiative et de performance"


  #print(text_N)
  #print("\n")
  #print(text_E)
  #print("\n")
  #print(text_O)
  #print("\n")
  #print(text_A)
  #print("\n")
  #print(text_C)
  #print("\n")
  #print(text_MD)
  #print("\n")
  #print(text_SC)
  #print("\n")
  #print(text_IC)
  #print("\n")
  #print(text_AI)
  #print("\n")
  #print(text_CC)
  #print("\n")
  #print(text_OE)
  #print("\n")
  #print(text_AG)
  #print("\n")
  #print(text_EP)
  #print("\n")

  #print("N : "+text_N)
  #print("E : "+text_E)
  #print("O : "+text_O)
  #print("A : "+text_A)
  #print("C : "+text_C)
  #print("AG : "+text_AG)
  #print("AI : "+text_AI)
  #print("CC : "+text_CC)
  #print("EP : "+text_EP)
  #print("IC : "+text_IC)
  #print("MD : "+text_MD)
  #print("OE : "+text_OE)
  #print("SC : "+text_SC)
  #print(TE3)

def create_circular_progress_bar(canvas, size, width):
    """Crée une barre de progression circulaire sur le canvas"""
    # Dessiner le cercle de fond
    canvas.create_oval(width, width, size - width, size - width, outline='lightgrey', width=width)

    # Arc de progression (qui sera animé)
    arc = canvas.create_arc(width, width, size - width, size - width, start=90, extent=0, outline='blue', style='arc',
                            width=width)

    # Texte au centre
    text = canvas.create_text(size / 2, size / 2 - 10, text='0%', font=('Arial', 13, 'bold'))  # Pourcentage
    niveau_text = canvas.create_text(size / 2, size / 2 + 10, text='Niveau: Faible', font=('Arial', 10))  # Niveau

    return arc, text, niveau_text

def get_progress_color(percentage):
    """Retourne une couleur en fonction du pourcentage de progression"""
    if percentage >= 64:
        return '#1479ff'
    elif 56 <= percentage < 64.99:
        return 'green'
    elif 45 <= percentage < 55.99:
        return 'lightgreen'
    elif 34 <= percentage < 44.99:
        return 'yellow'
    else:
        return 'orange'

def update_progress_bar(canvas, arc, text, niveau_text, value, max_value, size, width):
    """Met à jour l'arc de progression, le texte et la couleur en fonction du pourcentage"""
    percentage = (value / max_value) * 100
    extent = (value / max_value) * 360
    color = get_progress_color(percentage)  # Obtenir la couleur en fonction du pourcentage
    canvas.itemconfig(arc, extent=-extent, outline=color)  # Appliquer la couleur à l'arc
    canvas.itemconfig(text, text=f'{int(percentage)}%')

    # Mise à jour du niveau en fonction du pourcentage
    if percentage >= 64:
        niveau= 'tres eleve'
    elif 56 <= percentage < 64.99:
        niveau= 'eleve'
    elif 45 <= percentage < 55.99:
        niveau= 'moyen'
    elif 34 <= percentage < 44.99:
        niveau= 'faible'
    else:
        niveau= 'tres faible'

    canvas.itemconfig(niveau_text, text=f'{niveau}')

def animate_progress_bar(canvas, arc, text, niveau_text, target_percentage, speed, current_value, max_value, size,
                         width):
    """Anime la barre de progression vers le pourcentage cible"""
    current_percentage = (current_value / max_value) * 100
    if current_percentage < target_percentage:
        new_value = current_value + speed
        update_progress_bar(canvas, arc, text, niveau_text, new_value, max_value, size, width)
        # Continuer l'animation
        canvas.after(50, animate_progress_bar, canvas, arc, text, niveau_text, target_percentage, speed, new_value,
                     max_value, size, width)

def Hcreate_horizontal_progress_bar(canvas, width, height):
    """Crée une barre de progression horizontale sur le canvas"""
    # Dessiner le rectangle de fond
    canvas.create_rectangle(0, 0, width, height, outline='lightgrey', fill='lightgrey')

    # Rectangle de progression (qui sera animé)
    progress = canvas.create_rectangle(0, 0, 0, height, outline='red', fill='red')  # Couleur rouge

    # Texte au centre
    text = canvas.create_text(width / 2, height / 2, text='0%', font=('Arial', 13))

    return progress, text

def Hupdate_progress_bar(canvas, progress, text, value, max_value, width, height):
    """Met à jour la barre de progression et le texte"""
    progress_width = (value / max_value) * width
    canvas.coords(progress, 0, 0, progress_width, height)  # Met à jour les coordonnées du rectangle
    canvas.itemconfig(text, text=f'{int((value / max_value) * 100)}%')

    # Obtenir la couleur en fonction du pourcentage
    percentage = (value / max_value) * 100
    color = get_progress_color(percentage)  # Utiliser la fonction de couleur dynamique
    canvas.itemconfig(progress, outline=color, fill=color)  # Appliquer la couleur à la barre de progression

def Hanimate_progress_bar(canvas, progress, text, target_percentage, speed, current_value, max_value, width, height):
    """Anime la barre de progression vers le pourcentage cible"""
    current_percentage = (current_value / max_value) * 100
    if current_percentage < target_percentage:
        new_value = current_value + speed
        Hupdate_progress_bar(canvas, progress, text, new_value, max_value, width, height)
        # Continuer l'animation
        canvas.after(50, Hanimate_progress_bar, canvas, progress, text, target_percentage, speed, new_value, max_value, width, height)

def create_divided_progress_bar(canvas, width, height):
    """Crée une barre divisée en 5 parties égales avec des couleurs et du texte, décalée à droite"""
    
    # Largeur de chaque section (diviser en 5 parties)
    section_width = width // 5
    
    # Couleurs pour chaque section
    colors = ['orange', 'yellow', 'lightgreen', 'green', 'skyblue']
    
    # Textes pour chaque section
    texts = ['Très faible', 'Faible', 'Moyen', 'Élevé', 'Très élevé']
    
    # Dessiner chaque section avec sa couleur
    for i in range(5):
        x0 = i * section_width
        x1 = (i + 1) * section_width
        canvas.create_rectangle(x0, 0, x1, height, outline=colors[i], fill=colors[i])
        
        # Ajouter le texte au centre de chaque section
        canvas.create_text((x0 + x1) // 2, height // 2, text=texts[i], font=('Arial', 12), fill='black')

def create_divided_progress_barPDF(c, x, y):
    """Crée une barre divisée en 5 parties égales avec des couleurs et du texte."""
    total_width = 268
    height = 15
    section_width = total_width // 5
    colors = ['orange', 'yellow', 'lightgreen', 'green', '#87CEEB']  # Bleu ciel
    texts = ['Très faible', 'Faible', 'Moyen', 'Élevé', 'Très élevé']
    
    # Réduire la taille de la police
    c.setFont("Helvetica", 8)  # Taille de police réduite

    for i in range(5):
        c.setFillColor(colors[i])
        c.rect(x + i * section_width, y, section_width, height, stroke=0, fill=1)
        c.setFillColor("black")
        
        # Calculer la position du texte pour centrer horizontalement et verticalement
        text_x = x + i * section_width + (section_width - c.stringWidth(texts[i], "Helvetica", 8)) / 2
        text_y = y + (height - 8) / 2  # Ajustez 8 pour la taille de la police

        c.drawString(text_x, text_y, texts[i])

def create_progress_bar(progress):
    """Crée une barre de progression sous forme d'image temporaire avec le pourcentage à gauche."""
    progress_color = get_progress_color(progress)
    fig, ax = plt.subplots(figsize=(2, 0.3))  # Taille de la figure
    ax.barh(0, progress, color=progress_color, height=0.3)
    ax.barh(0, 100 - progress, left=progress, color='#E0E0E0', height=0.3)

    # Positionner le pourcentage à gauche de la barre de progression
    ax.text(-10, 0, f"{progress}%", ha="right", va="center", fontsize=10, color=get_progress_color(progress), fontname="Arial")

    ax.set_xlim(0, 100)
    ax.axis("off")

    with NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
        plt.savefig(temp_image.name, format="PNG", bbox_inches='tight', pad_inches=0.1, dpi=300)
        temp_image_path = temp_image.name
    plt.close(fig)
    return temp_image_path


def create_progress_ring(progress):
    """Crée un anneau de progression sous forme d'image temporaire"""
    progress_color = get_progress_color(progress)
    fig, ax = plt.subplots(figsize=(2, 2), subplot_kw=dict(aspect="equal"))
    colors = [progress_color, '#E0E0E0']
    data = [progress, 100 - progress]
    
    ax.pie(data, startangle=90, colors=colors, radius=1.0, wedgeprops=dict(width=0.3))
    ax.text(0, 0, f"{progress}%", ha="center", va="center", fontsize=20, color="#333333")
    with NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
        plt.savefig(temp_image.name, format="PNG")
        temp_image_path = temp_image.name
    plt.close(fig)
    return temp_image_path

def wrap_text(text, width, c, x, y):
    """Retourne le texte en plusieurs lignes sans dépasser la largeur spécifiée,
    en découpant les mots s'ils sont trop longs pour tenir dans la largeur."""
    
    words = text.split(' ')
    line = ''
    
    for word in words:
        # Si le mot seul dépasse la largeur, on doit le couper
        while c.stringWidth(word, "Helvetica", 12) > width:
            # Trouve le nombre de caractères qui tiennent dans la largeur
            i = 0
            while c.stringWidth(word[:i + 1], "Helvetica", 12) < width:
                i += 1
            # Ajoute la portion du mot qui tient dans la ligne
            line = word[:i]
            c.drawString(x, y, line)
            y -= 15
            # Coupe le mot et continue avec le reste
            word = word[i:]
        
        # Si ajouter le mot actuel dépasse la largeur, dessine la ligne actuelle et commence une nouvelle ligne
        if c.stringWidth(line + word, "Helvetica", 12) > width:
            c.drawString(x, y, line)
            y -= 15
            line = word + ' '
        else:
            # Continue d'ajouter des mots à la ligne tant que cela tient dans la largeur
            line += word + ' '
    
    # Dessine la dernière ligne si elle n'est pas vide
    if line:
        c.drawString(x, y, line)
        y -= 15
    
    return y

def open_pdf(file_path):
    if platform.system() == "Windows":
        os.startfile(file_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["open", file_path])
    else:  # Linux
        subprocess.call(["xdg-open", file_path])
    print("fichier ouvert !")

def create_pdf(filename, traits, traits2, traits3, traits4, candidate_info, patho):
    nomfiche = "Rapport_" + filename + ".pdf"
    c = canvas.Canvas(nomfiche, pagesize=letter)
    width, height = letter
    top_margin = 50    # Marge en haut de la page
    bottom_margin = 70 # Marge en bas de la page
    y = height - top_margin  # Ajuste la position y pour commencer à dessiner après la marge en haut

    # Ajout d'un grand titre
    c.setFont("Helvetica-Bold", 24)
    c.drawString(30, y, "Rapport du test de personnalité")
    c.line(30, y - 5, width - 30, y - 5)  # Ligne sous le titre
    y -= 40  # Ajuste pour le début du contenu après le titre et la ligne

    # Informations du candidat
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Informations du candidat :")
    y -= 25

    # Ajouter les informations du candidat (nom, prénom, âge, sexe)
    c.setFont("Helvetica", 12)
    for label, info in candidate_info.items():
        c.drawString(30, y, f"{label}: {info}")
        y -= 15

    y -= 70  # Espace après les informations du candidat

    # Les Cinq Grands Traits De La Personnalité
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Les Cinq Grands Traits De La Personnalité:")
    y -= 25

    for title, text, progress in traits:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(30, y, title)
        y -= 25
        c.setFont("Helvetica", 12)
        wrap_width = width * 0.7
        y = wrap_text(text, wrap_width - 60, c, 30, y)

        ring_image_path = create_progress_ring(progress)
        ring_width = 100
        c.drawImage(ring_image_path, width - ring_width - 30, y - 10, width=ring_width, height=100)
        y -= 50

        if y < bottom_margin:
            c.showPage()
            y = height - top_margin

    y -= 70
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Les Huit Compétences:")
    y -= 50

    divided_bar_x_position = 300
    create_divided_progress_barPDF(c, divided_bar_x_position, y - 5)
    y -= 30

    for title, progress in traits2:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(30, y, title)
        y -= 10

        bar_image_path = create_progress_bar(progress)
        bar_width = 300
        c.drawImage(bar_image_path, width - bar_width - 30, y - 10, width=bar_width, height=30)
        y -= 30

        if y < bottom_margin:
            c.showPage()
            y = height - top_margin

    y -= 70
    for title, text in traits3:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(30, y, title)
        y -= 25

        c.setFont("Helvetica", 12)
        y = wrap_text(text, width - 100, c, 30, y)

        y -= 15
        y -= 50
        if y < bottom_margin:
            c.showPage()
            y = height - top_margin

    y -= 70

    c.save()
    open_pdf(nomfiche)
    print("PDF créé")
    creat_pdf_patho(filename, traits4, candidate_info, patho)

def create_graph_image(patho):
    # Données pour le graphique
    x = list(range(1, 36))
    y = patho
    x_labels = [
        "Névrosisme TN", "Anxiété TN1", "Colère - Hostilité TN2", "Dépression TN3", "Timidité Sociale TN4", "Impulsivité TN5", "Vulnérabilité TN6",
        "Extraversion TE", "Chaleur TE1", "Grégarité TE2", "Assertivité TE3", "Activité TE4", "Rech- sensations TE5", "Emotions posit TE6",
        "Ouverture TO", "Réveries TO1", "Esthétique TO2", "Sentiments TO3", "Actions TO4", "Idées TO5", "Valeur TO",
        "Agréabilité TA", "Confiance TA1", "Droiture TA2", "Altruisme TA3", "Compliance TA4", "Modestie TA5", "Sensibilité TA6",
        "Conscience TC", "Compétence TC1", "Ordre TC2", "Sens du devoir TC3", "Rech , réussite TC4", "Autodiscipline TC5", "Délibération TC6"
    ]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, marker='o', color='b', linestyle='-', linewidth=2, markersize=5)
    ax.set_title("Graphique des Pathologies")
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, rotation=90, ha='center', fontsize=8)

    # Sauvegarder le graphique comme image temporaire
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig.savefig(temp_file.name, bbox_inches="tight")
    plt.close(fig)  # Fermer la figure après l'avoir enregistrée pour libérer de la mémoire

    return temp_file.name

def creat_pdf_patho(filename, traits, candidate_info, patho):
    nomfiche = "Pathologie_" + filename + ".pdf"
    c = canvas.Canvas(nomfiche, pagesize=letter)
    width, height = letter
    top_margin = 50    # Marge en haut de la page
    bottom_margin = 70 # Marge en bas de la page
    y = height - top_margin  # Position initiale pour le contenu

    # Ajouter un grand titre
    c.setFont("Helvetica-Bold", 24)
    c.drawString(30, y, "Rapport de Pathologie")
    c.line(30, y - 5, width - 30, y - 5)
    y -= 40  # Ajuste pour le début du contenu après le titre et la ligne

    # Informations du candidat
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y, "Informations du candidat :")
    y -= 25

    c.setFont("Helvetica", 12)
    for label, info in candidate_info.items():
        c.drawString(30, y, f"{label}: {info}")
        y -= 15

    y -= 70  # Espace après les informations du candidat
    graph_image_path = create_graph_image(patho)
    c.drawImage(graph_image_path, 30, y - 250, width=500, height=250)

    y -= 300  # Espace apres la pathologie
    # Pathologie
    for title, text in traits:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(30, y, title)
        y -= 15

        c.setFont("Helvetica", 12)
        y = wrap_text(text, width - 100, c, 30, y)
        y -= 15
        y -= 50

        if y < bottom_margin:
            c.showPage()
            y = height - top_margin

    # Créer et insérer le graphique
    
    #y -= 300  # Ajuster l'espace avant le graphique
    #if y < 250:
        #c.showPage()
        #y = height - top_margin - 300

    

    # Enregistrer et nettoyer
    c.save()
    os.remove(graph_image_path)
    open_pdf(nomfiche)
    print(f"PDF créé : {nomfiche}")

# Afficher le rapport des réponses
def show_report():
    clear_window()
    calcul()

    genre = "Homme" if sexe.get() == "H" else "Femme"

    

    # Créer une frame pour le défilement
    frame = tk.Frame(root)
    frame.pack(pady=20, fill=tk.BOTH, expand=True)

    # Ajouter une barre de défilement
    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Afficher les informations personnelles dans le rapport
    label_responses_title = ttk.Label(scrollable_frame, text="Rapport du test de personnalité :",
                                      font=("Helvetica", 16, 'bold'), padding=(20, 20))
    label_responses_title.pack()

    labels = ttk.Label(scrollable_frame, text="\n\n", font=("Helvetica", 14))
    labels.pack()

    info={
       "Nom": nom.get(),
    "Prénom": prenom.get(),
    "Âge": age.get(),
    "Sexe": genre
    }

    
    label_info = ttk.Label(scrollable_frame, text=f"Nom: {nom.get()}\nPrénom: {prenom.get()}\nÂge: {age.get()}\nSexe: {genre}",
                           font=("Helvetica", 16, 'bold'), padding=(20, 20))
    label_info.pack(anchor='w', padx=(20, 0), pady=(20, 10))

   
    
    # Liste des traits et leurs valeurs cibles
    traits = [
        ("NEVROSITE", text_N, NEV),
        ("EXTRAVERSION", text_E, EXT),
        ("OUVERTURE", text_O, OUV),
        ("AGRÉABILITÉ", text_A, AGR),
        ("CONSCIENCE", text_C, CON),
    ]

    label_competence = ttk.Label(scrollable_frame, text="Résumé des scores aux cinq grands traits:",
                                  font=("Helvetica", 16, 'bold'), padding=(20, 20))
    label_competence.pack()

    # Créer des barres de progression circulaires pour chaque trait
    for trait_name, text_value, target_percentage in traits:
        # Créer une frame pour tenir le label et la barre de progression
        trait_frame = tk.Frame(scrollable_frame)
        trait_frame.pack(fill='x', pady=(5, 5))

        # Set the title label with bold and underline, aligned to the left and centered vertically
        labeln = ttk.Label(trait_frame, text=trait_name, font=("Helvetica", 14, 'bold', 'underline'), padding=(20, 5))
        labeln.pack(side='left', anchor='w')  # Aligné à gauche (west)

        # Add the explanatory text with reduced wraplength, also aligned to the left
        text_label = ttk.Label(trait_frame, text=text_value, font=("Helvetica", 14), padding=(5, 5), wraplength=600)
        text_label.pack(side='left', anchor='w', padx=(5, 20))

        # Create a canvas for the circular progress bar and align it to the right
        canvas_size = 150  # Size of the progress bar
        progress_canvas = tk.Canvas(trait_frame, width=canvas_size, height=canvas_size)
        progress_canvas.pack(side='right', padx=(10, 0))  # Aligner à droite

        # Create the circular progress bar
        arc, text, niveau_text = create_circular_progress_bar(progress_canvas, canvas_size, 17)
        animate_progress_bar(progress_canvas, arc, text, niveau_text, target_percentage, speed=1, current_value=0,
                              max_value=100, size=canvas_size, width=17)

    labels = ttk.Label(scrollable_frame, text="\n\n", font=("Helvetica", 14))
    labels.pack()

    # Indices des huit grandes compétences
    label_competence = ttk.Label(scrollable_frame, text="Indices des huit grandes compétences :",
                                  font=("Helvetica", 16, 'bold'), padding=(20, 20))
    label_competence.pack()

    # Créer une frame pour la barre divisée et les barres horizontales
    divided_frame = tk.Frame(scrollable_frame)
    divided_frame.pack(anchor='e', pady=(5, 5))  # Aligner le frame à droite
  
    # Créer le canvas pour la barre divisée
    canvas_width = 400
    canvas_height = 30
    canvasd = tk.Canvas(divided_frame, width=canvas_width, height=canvas_height)
    canvasd.pack(side='right', pady=(10, 10), padx=(10, 0))  # Aucune nécessité de padding horizontal ici
    
    create_divided_progress_bar(canvasd, canvas_width, canvas_height)


    labels = ttk.Label(scrollable_frame, text="\n\n", font=("Helvetica", 14))
    labels.pack()

    # Créer des barres de progression horizontales
    additional_traits = [
        ("MENNER ET DÉCIDER", MD),
        ("SOUTENIR ET COOPÉRER", SC),
        ("INTERAGIR ET COMMUNIQUER", IC),
        ("ANALYSER ET INTERPRÉTER", AI),
        ("CRÉER ET CONCEPTUALISER", CC),
        ("ORGANISER ET EXÉCUTER", OE),
        ("ADAPTER ET GÉRER LA PRESSION", AG),
        ("ENTREPRENDRE ET PERFORMER", EP),
    ]
    
    for trait_name, target_percentage in additional_traits:
        # Créer une frame pour contenir le label et la barre de progression
        h_trait_frame = tk.Frame(scrollable_frame)
        h_trait_frame.pack(fill='x', pady=10)  # Remplir horizontalement

        # Créer un label pour le titre et l'aligner à gauche
        h_label = ttk.Label(h_trait_frame, text=trait_name, font=("Helvetica", 14, 'bold', 'underline'), padding=(5, 5))
        h_label.pack(side='left', anchor='w')  # Aligner le titre à gauche

        # Créer un canvas pour dessiner la barre de progression horizontale et l'aligner à droite
        h_canvas = tk.Canvas(h_trait_frame, width=400, height=30)
        h_canvas.pack(side='right', pady=(10, 10), padx=(10, 0))  # Aligner la barre à droite

        # Créer la barre de progression horizontale
        progress, text = Hcreate_horizontal_progress_bar(h_canvas, 400, 30)

        # Lancer l'animation pour remplir la barre jusqu'au pourcentage cible
        Hanimate_progress_bar(h_canvas, progress, text, target_percentage, speed=1, current_value=0, max_value=100, width=400, height=30)

    additional_traits2 = [
        ("MENNER ET DÉCIDER", text_MD),
        ("SOUTENIR ET COOPÉRER", text_SC),
        ("INTERAGIR ET COMMUNIQUER", text_IC),
        ("ANALYSER ET INTERPRETER",text_AI ),
        ("CRÉER ET CONCEPTUALISER",text_CC),
        ("ORGANISER ET EXÉCUTER",text_OE ),
        ("ADAPTER ET GERER LA PRESSION",text_AG),
        ("ENTREPRENDRE ET PERFORMER",text_EP),
    ]
    for trait_name, text_value,  in additional_traits2:
        # Créer une frame pour tenir le label et la barre de progression
        trait_frame = tk.Frame(scrollable_frame)
        trait_frame.pack(anchor='w', pady=(5, 5))

        # Set the title label with bold and underline
        labela = ttk.Label(trait_frame, text=trait_name, font=("Helvetica", 14, 'bold', 'underline'), padding=(20, 5))
        labela.pack(side='left')

        # Add the explanatory text with reduced wraplength
        text_label2 = ttk.Label(trait_frame, text=text_value, font=("Helvetica", 14), padding=(5, 5), wraplength=600)
        text_label2.pack(side='left', padx=(5, 20))

    LESION = [
        ("Anxiété", text_TN1),
        ("Colère - Hostilité", text_TN2),
        ("Dépression",text_TN3 ),
        ("Timidité Sociale", text_TN4),
        ("Impulsivité",text_TN5 ),
        ("Vulnérabilité",text_TN6),
        ("Chaleur",text_TE1 ),
        ("Grégarité",text_TE2),
        ("Assertivité",text_TE3),
        ("Activité",text_TE4),
        ("Rech- sensations",text_TE5),
        ("Emotions positive",text_TE6),
        ("Réveries", text_TO1),
        ("Esthétique", text_TO2),
        ("Sentiments",text_TO3 ),
        ("Actions", text_TO4),
        ("Idées",text_TO5 ),
        ("Valeur",text_TO6),
        ("Confiance",text_TA1 ),
        ("Droiture",text_TA2),
        ("Altruisme",text_TA3),
        ("Compliance",text_TA4),
        ("Modestie",text_TA5),
        ("Sensibilité",text_TA6),
        ("Compétence",text_TC1 ),
        ("Ordre",text_TC2),
        ("Sens du devoir",text_TC3),
        ("Rech - réussite",text_TC4),
        ("Autodiscipline",text_TC5),
        ("Délibération",text_TC6),

        
        
    ]
    for lesion_name, text_value,  in LESION:
        # Créer une frame pour tenir le label et la barre de progression
        lesion_frame = tk.Frame(scrollable_frame)
        lesion_frame.pack(anchor='w', pady=(5, 5))

        # Set the title label with bold and underline
        labell = ttk.Label(lesion_frame, text=lesion_name, font=("Helvetica", 14, 'bold', 'underline'), padding=(20, 5))
        labell.pack(side='left')

        # Add the explanatory text with reduced wraplength
        text_labell = ttk.Label(lesion_frame, text=text_value, font=("Helvetica", 14), padding=(5, 5), wraplength=600)
        text_labell.pack(side='left', padx=(5, 20))

        # Configurer la barre de défilement
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.configure(yscrollcommand=scrollbar.set)
    #affichage des different paramettre sur l'interface !
    #score=[
    #  ("N",N),
    #  ("E",E),
    #  ("O",O),
    #  ("A",A),
    #  ("C",C),
    #  ("N1",N1),
    #  ("N2",N2),
    #  ("N3",N3),
    #  ("N4",N4),
    #  ("N5",N5),
    #  ("N6",N6),
    #  ("E1",E1),
    #  ("E2",E2),
    #  ("E3",E3),
    #  ("E4",E4),
    #  ("E5",E5),
    #  ("E6",E6),
    #  ("O1",O1), 
    #  ("O2",O2),
    #  ("O3",O3),
    #  ("O4",O4),
    #  ("O5",O5),
    #  ("O6",O6),
    #  ("A1",A1),
    #  ("A2",A2),
    #  ("A3",A3),
    #  ("A4",A4),
    #  ("A5",A5),
    #  ("A6",A6),
    #  ("C1",C1),
    #  ("C2",C2),
    #  ("C3",C3),
    #  ("C4",C4),
    #  ("C5",C5),
    #  ("C6",C6),
    #  #("TN",TN),
    #  #("TE",TE),
    #  #("TO",TO),
    #  #("TA",TA),
    #  #("TC",TC),
    #  ("TN1",TN1),
    #  ("TN2",TN2),
    #  ("TN3",TN3),
    #  ("TN4",TN4),
    #  ("TN5",TN5),
    #  ("TN6",TN6),
    #  ("TE1",TE1),
    #  ("TE2",TE2),
    #  ("TE3",TE3),
    #  ("TE4",TE4),
    #  ("TE5",TE5),
    #  ("TE6",TE6),
    #  ("TO1",TO1), 
    #  ("TO2",TO2),
    #  ("TO3",TO3),
    #  ("TO4",TO4),
    #  ("TO5",TO5),
    #  ("TO6",TO6),
    #  ("TA1",TA1),
    #  ("TA2",TA2),
    #  ("TA3",TA3),
    #  ("TA4",TA4),
    #  ("TA5",TA5),
    #  ("TA6",TA6),
    #  ("TC1",TC1),
    #  ("TC2",TC2),
    #  ("TC3",TC3),
    #  ("TC4",TC4),
    #  ("TC5",TC5),
    #  ("TC6",TC6),
    #  ("MENNER ET DÉCIDER", MD),
    #  ("SOUTENIR ET COOPÉRER", SC),
    #  ("INTERAGIR ET COMMUNIQUER", IC),
    #  ("ANALYSER ET INTERPRÉTER", AI),
    #  ("CRÉER ET CONCEPTUALISER", CC),
    #  ("ORGANISER ET EXÉCUTER", OE),
    #  ("ADAPTER ET GÉRER LA PRESSION", AG),
    #  ("ENTREPRENDRE ET PERFORMER", EP)
    #]
    #for label, value in score:
    #  frame = tk.Frame(scrollable_frame)
    #  frame.pack(fill="x", padx=10, pady=2)
    #  tk.Label(frame, text=label, font=('Arial', 10, 'bold')).pack(side="left")
    #  tk.Label(frame, text=value, font=('Arial', 10)).pack(side="left")

    # Lier la molette de la souris pour faire défiler
    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    # Dictionnaire pour stocker les questions par lettre
    questions_par_lettre = {"Pas du tout d'accord": [], "Pas d'accord": [], "Neutre": [], "D'accord": [], "Tout à fait d'accord": []}

    for i, reponse in enumerate(responses):
        if reponse == 1:
            questions_par_lettre["Pas du tout d'accord"].append(i + 1)
        elif reponse == 2:
            questions_par_lettre["Pas d'accord"].append(i + 1)
        elif reponse == 3:
            questions_par_lettre["Neutre"].append(i + 1)
        elif reponse == 4:
            questions_par_lettre["D'accord"].append(i + 1)
        elif reponse == 5:
            questions_par_lettre["Tout à fait d'accord"].append(i + 1)

    for lettre, questions in questions_par_lettre.items():
        print(f"Réponse {lettre} choisie pour les questions : {questions}")

    #Calcule taux du choix fortement d'accord
    Taux_Fdac = (len(questions_par_lettre["Tout à fait d'accord"]) / 240)*100
    print(f"Taux de réponses 'Tout à fait d'accord': {Taux_Fdac:.2%}")

    #Calcule taux du choix d'accord
    Taux_Dac = (len(questions_par_lettre["D'accord"]) / 240)*100
    print(f"Taux de réponses 'D'accord': {Taux_Dac:.2%}")

    #Calcule taux du choix neutre
    Taux_Ntr = (len(questions_par_lettre["Neutre"]) / 240)*100
    print(f"Taux de réponses 'Neutre': {Taux_Ntr:.2%}")

    #Calcule taux du choix pas d'accord
    Taux_PDac = (len(questions_par_lettre["Pas d'accord"]) / 240)*100
    print(f"Taux de réponses 'Pas d'accord': {Taux_PDac:.2%}")

    #Calcule taux du choix pas du tout d'accord
    Taux_PDDac = (len(questions_par_lettre["Pas du tout d'accord"]) / 240)*100
    print(f"Taux de réponses 'Pas du tout d'accord': {Taux_PDDac:.2%}")
    # Affichage des taux dans l'interface graphique
    taux_frame = tk.Frame(scrollable_frame)
    taux_frame.pack(pady=(20, 10), fill='x')
    label_titre_taux = ttk.Label(taux_frame, text="Les taux des choix du candidat :", font=("Helvetica", 16, 'bold'), padding=(10, 10))
    label_titre_taux.pack(anchor='w')

    label_taux_fdac = ttk.Label(taux_frame, text=f"Taux 'Tout à fait d'accord' : {Taux_Fdac:.2f}%", font=("Helvetica", 14))
    label_taux_fdac.pack(anchor='w')
    label_taux_dac = ttk.Label(taux_frame, text=f"Taux 'D'accord' : {Taux_Dac:.2f}%", font=("Helvetica", 14))
    label_taux_dac.pack(anchor='w')
    label_taux_ntr = ttk.Label(taux_frame, text=f"Taux 'Neutre' : {Taux_Ntr:.2f}%", font=("Helvetica", 14))
    label_taux_ntr.pack(anchor='w')
    label_taux_pdac = ttk.Label(taux_frame, text=f"Taux 'Pas d'accord' : {Taux_PDac:.2f}%", font=("Helvetica", 14))
    label_taux_pdac.pack(anchor='w')
    label_taux_pddac = ttk.Label(taux_frame, text=f"Taux 'Pas du tout d'accord' : {Taux_PDDac:.2f}%", font=("Helvetica", 14))
    label_taux_pddac.pack(anchor='w')

    button_frame = ttk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=20)
    PATHO = [NEV,EXT,OUV,AGR,CON,TN1,TN2,TN3,TN4,TN5,TN6,TE1,TE2,TE3,TE4,TE5,TE6,TO1,TO2,TO3,TO4,TO5,TO6,TA1,TA2,TA3,TA4,TA5,TA6,TC1,TC2,TC3,TC4,TC5,TC6] 
    # Bouton Créer PDF
    button_create_pdf = ttk.Button(button_frame, text="Cree PDF", command=lambda: create_pdf(f"{nom.get()}_{prenom.get()}", traits, additional_traits, additional_traits2, LESION, info,PATHO), width=20)
    button_create_pdf.pack(side=tk.LEFT, padx=5)  # Utiliser side=tk.LEFT pour les placer côte à côte
    # Bouton Quitter
    button_exit = ttk.Button(button_frame, text="Quitter", command=root.quit, width=20)
    button_exit.pack(side=tk.LEFT, padx=5)  # Utiliser side=tk.LEFT pour les placer côte à côte

# Launch the interface with the introduction screen
introduction_screen()
root.mainloop()




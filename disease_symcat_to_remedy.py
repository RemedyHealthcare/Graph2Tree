import cPickle as pickle

a = {
	u'/conditions/abdominal-aortic-aneurysm': 488,
	u'/conditions/abdominal-hernia': 528,
	u'/conditions/abscess-of-nose': 175,
	u'/conditions/abscess-of-the-lung': 215,
	u'/conditions/abscess-of-the-pharynx': 613,
	u'/conditions/acanthosis-nigricans': 122,
	u'/conditions/acariasis': 196,
	u'/conditions/achalasia': 399,
	u'/conditions/acne': 633,
	u'/conditions/actinic-keratosis': 127,
	u'/conditions/acute-bronchiolitis': 392,
	u'/conditions/acute-bronchitis': 524,
	u'/conditions/acute-bronchospasm': 220,
	u'/conditions/acute-fatty-liver-of-pregnancy-aflp': 48,
	u'/conditions/acute-glaucoma': 139,
	u'/conditions/acute-kidney-injury': 304,
	u'/conditions/acute-otitis-media': 616,
	u'/conditions/acute-pancreatitis': 267,
	u'/conditions/acute-respiratory-distress-syndrome-ards': 131,
	u'/conditions/acute-sinusitis': 341,
	u'/conditions/acute-stress-reaction': 152,
	u'/conditions/adhesive-capsulitis-of-the-shoulder': 11,
	u'/conditions/adjustment-reaction': 133,
	u'/conditions/adrenal-adenoma': 343,
	u'/conditions/adrenal-cancer': 29,
	u'/conditions/air-embolism': 287,
	u'/conditions/alcohol-abuse': 250,
	u'/conditions/alcohol-intoxication': 766,
	u'/conditions/alcohol-withdrawal': 278,
	u'/conditions/alcoholic-liver-disease': 326,
	u'/conditions/allergy': 138,
	u'/conditions/allergy-to-animals': 202,
	u'/conditions/alopecia': 336,
	u'/conditions/alzheimer-disease': 108,
	u'/conditions/amblyopia': 369,
	u'/conditions/amyloidosis': 600,
	u'/conditions/amyotrophic-lateral-sclerosis-als': 264,
	u'/conditions/anal-fissure': 417,
	u'/conditions/anal-fistula': 135,
	u'/conditions/anemia': 433,
	u'/conditions/anemia-due-to-chronic-kidney-disease': 187,
	u'/conditions/anemia-due-to-malignancy': 65,
	u'/conditions/anemia-of-chronic-disease': 391,
	u'/conditions/angina': 782,
	u'/conditions/ankylosing-spondylitis': 644,
	u'/conditions/anxiety': 350,
	u'/conditions/aortic-valve-disease': 261,
	u'/conditions/aphakia': 386,
	u'/conditions/aphthous-ulcer': 21,
	u'/conditions/aplastic-anemia': 130,
	u'/conditions/appendicitis': 37,
	u'/conditions/arrhythmia': 143,
	u'/conditions/arthritis-of-the-hip': 568,
	u'/conditions/ascending-cholangitis': 673,
	u'/conditions/asperger-syndrome': 724,
	u'/conditions/aspergillosis': 157,
	u'/conditions/asthma': 422,
	u'/conditions/astigmatism': 243,
	u'/conditions/atelectasis': 734,
	u'/conditions/athlete-s-foot': 769,
	u'/conditions/atonic-bladder': 595,
	u'/conditions/atrial-fibrillation': 226,
	u'/conditions/atrial-flutter': 254,
	u'/conditions/atrophic-skin-condition': 728,
	u'/conditions/atrophic-vaginitis': 221,
	u'/conditions/atrophy-of-the-corpus-cavernosum': 469,
	u'/conditions/attention-deficit-hyperactivity-disorder-adhd': 188,
	u'/conditions/autism': 281,
	u'/conditions/autonomic-nervous-system-disorder': 432,
	u'/conditions/avascular-necrosis': 9,
	u'/conditions/balanitis': 34,
	u'/conditions/behcet-disease': 137,
	u'/conditions/bell-palsy': 106,
	u'/conditions/benign-kidney-cyst': 482,
	u'/conditions/benign-paroxysmal-positional-vertical-bppv': 19,
	u'/conditions/benign-prostatic-hyperplasia-bph': 186,
	u'/conditions/benign-vaginal-discharge-leukorrhea': 780,
	u'/conditions/bipolar-disorder': 578,
	u'/conditions/birth-trauma': 284,
	u'/conditions/bladder-cancer': 553,
	u'/conditions/bladder-disorder': 151,
	u'/conditions/bladder-obstruction': 381,
	u'/conditions/blastomycosis': 270,
	u'/conditions/blepharitis': 266,
	u'/conditions/blepharospasm': 61,
	u'/conditions/bone-cancer': 385,
	u'/conditions/bone-disorder': 475,
	u'/conditions/bone-spur-of-the-calcaneous': 94,
	u'/conditions/brachial-neuritis': 667,
	u'/conditions/brain-cancer': 285,
	u'/conditions/breast-cancer': 153,
	u'/conditions/breast-cyst': 42,
	u'/conditions/breast-infection-mastitis': 45,
	u'/conditions/broken-tooth': 253,
	u'/conditions/bronchiectasis': 777,
	u'/conditions/bruise': 670,
	u'/conditions/bunion': 322,
	u'/conditions/burn': 768,
	u'/conditions/bursitis': 491,
	u'/conditions/callus': 471,
	u'/conditions/carbon-monoxide-poisoning': 242,
	u'/conditions/carcinoid-syndrome': 244,
	u'/conditions/cardiac-arrest': 401,
	u'/conditions/cardiomyopathy': 104,
	u'/conditions/carpal-tunnel-syndrome': 519,
	u'/conditions/cat-scratch-disease': 426,
	u'/conditions/cataract': 294,
	u'/conditions/celiac-disease': 508,
	u'/conditions/cellulitis-or-abscess-of-mouth': 566,
	u'/conditions/central-atherosclerosis': 437,
	u'/conditions/central-retinal-artery-or-vein-occlusion': 383,
	u'/conditions/cerebral-edema': 619,
	u'/conditions/cerebral-palsy': 504,
	u'/conditions/cervical-cancer': 333,
	u'/conditions/cervical-disorder': 349,
	u'/conditions/cervicitis': 625,
	u'/conditions/chagas-disease': 269,
	u'/conditions/chalazion': 296,
	u'/conditions/chancroid': 416,
	u'/conditions/chickenpox': 178,
	u'/conditions/chlamydia': 441,
	u'/conditions/cholecystitis': 162,
	u'/conditions/choledocholithiasis': 308,
	u'/conditions/cholesteatoma': 255,
	u'/conditions/chondromalacia-of-the-patella': 705,
	u'/conditions/chorioretinitis': 402,
	u'/conditions/chronic-back-pain': 86,
	u'/conditions/chronic-constipation': 695,
	u'/conditions/chronic-glaucoma': 334,
	u'/conditions/chronic-inflammatory-demyelinating-polyneuropathy-cidp': 532,
	u'/conditions/chronic-kidney-disease': 58,
	u'/conditions/chronic-knee-pain': 27,
	u'/conditions/chronic-obstructive-pulmonary-disease-copd': 397,
	u'/conditions/chronic-otitis-media': 116,
	u'/conditions/chronic-pain-disorder': 231,
	u'/conditions/chronic-pancreatitis': 47,
	u'/conditions/chronic-rheumatic-fever': 307,
	u'/conditions/chronic-sinusitis': 709,
	u'/conditions/chronic-ulcer': 726,
	u'/conditions/cirrhosis': 229,
	u'/conditions/coagulation-bleeding-disorder': 509,
	u'/conditions/cold-sore': 291,
	u'/conditions/colonic-polyp': 79,
	u'/conditions/colorectal-cancer': 421,
	u'/conditions/common-cold': 685,
	u'/conditions/complex-regional-pain-syndrome': 430,
	u'/conditions/concussion': 149,
	u'/conditions/conduct-disorder': 148,
	u'/conditions/conductive-hearing-loss': 213,
	u'/conditions/congenital-heart-defect': 448,
	u'/conditions/congenital-malformation-syndrome': 249,
	u'/conditions/congenital-rubella': 141,
	u'/conditions/conjunctivitis': 761,
	u'/conditions/conjunctivitis-due-to-allergy': 233,
	u'/conditions/conjunctivitis-due-to-bacteria': 289,
	u'/conditions/conjunctivitis-due-to-virus': 792,
	u'/conditions/connective-tissue-disorder': 744,
	u'/conditions/contact-dermatitis': 445,
	u'/conditions/conversion-disorder': 393,
	u'/conditions/cornea-infection': 534,
	u'/conditions/corneal-abrasion': 443,
	u'/conditions/corneal-disorder': 716,
	u'/conditions/coronary-atherosclerosis': 620,
	u'/conditions/cranial-nerve-palsy': 512,
	u'/conditions/crohn-disease': 687,
	u'/conditions/croup': 361,
	u'/conditions/crushing-injury': 459,
	u'/conditions/cryptococcosis': 311,
	u'/conditions/cryptorchidism': 342,
	u'/conditions/cushing-syndrome': 590,
	u'/conditions/cyst-of-the-eyelid': 163,
	u'/conditions/cystic-fibrosis': 241,
	u'/conditions/cysticercosis': 572,
	u'/conditions/cystitis': 50,
	u'/conditions/cytomegalovirus-infection': 632,
	u'/conditions/de-quervain-disease': 608,
	u'/conditions/decubitus-ulcer': 192,
	u'/conditions/deep-vein-thrombosis-dvt': 794,
	u'/conditions/degenerative-disc-disease': 759,
	u'/conditions/delirium': 251,
	u'/conditions/dementia': 306,
	u'/conditions/dengue-fever': 112,
	u'/conditions/dental-caries': 725,
	u'/conditions/depression--2': 526,
	u'/conditions/dermatitis-due-to-sun-exposure': 105,
	u'/conditions/developmental-disability': 268,
	u'/conditions/deviated-nasal-septum': 468,
	u'/conditions/diabetes': 330,
	u'/conditions/diabetes-insipidus': 109,
	u'/conditions/diabetic-ketoacidosis': 117,
	u'/conditions/diabetic-kidney-disease': 1,
	u'/conditions/diabetic-peripheral-neuropathy': 371,
	u'/conditions/diabetic-retinopathy': 228,
	u'/conditions/diaper-rash--2': 348,
	u'/conditions/dislocation-of-the-ankle': 123,
	u'/conditions/dislocation-of-the-elbow': 752,
	u'/conditions/dislocation-of-the-finger': 565,
	u'/conditions/dislocation-of-the-foot': 772,
	u'/conditions/dislocation-of-the-hip': 219,
	u'/conditions/dislocation-of-the-knee': 541,
	u'/conditions/dislocation-of-the-patella': 579,
	u'/conditions/dislocation-of-the-shoulder': 408,
	u'/conditions/dislocation-of-the-vertebra': 263,
	u'/conditions/dislocation-of-the-wrist': 164,
	u'/conditions/dissociative-disorder': 189,
	u'/conditions/diverticulitis': 636,
	u'/conditions/diverticulosis': 69,
	u'/conditions/down-syndrome': 147,
	u'/conditions/drug-abuse--2': 753,
	u'/conditions/drug-abuse-barbiturates': 654,
	u'/conditions/drug-abuse-cocaine': 259,
	u'/conditions/drug-abuse-methamphetamine': 477,
	u'/conditions/drug-abuse-opioids': 103,
	u'/conditions/drug-poisoning-due-to-medication': 145,
	u'/conditions/drug-reaction': 288,
	u'/conditions/drug-withdrawal': 121,
	u'/conditions/dry-eye-of-unknown-cause': 424,
	u'/conditions/dumping-syndrome': 555,
	u'/conditions/dyshidrosis': 57,
	u'/conditions/dysthymic-disorder': 182,
	u'/conditions/ear-drum-damage': 693,
	u'/conditions/ear-wax-impaction': 75,
	u'/conditions/eating-disorder': 640,
	u'/conditions/ectopic-pregnancy': 428,
	u'/conditions/ectropion': 340,
	u'/conditions/eczema': 557,
	u'/conditions/edward-syndrome': 778,
	u'/conditions/emphysema': 681,
	u'/conditions/empyema': 140,
	u'/conditions/encephalitis': 545,
	u'/conditions/endocarditis': 732,
	u'/conditions/endometrial-cancer': 184,
	u'/conditions/endometrial-hyperplasia': 209,
	u'/conditions/endometriosis': 200,
	u'/conditions/endophthalmitis': 431,
	u'/conditions/envenomation-from-spider-or-animal-bite': 755,
	u'/conditions/ependymoma': 643,
	u'/conditions/epididymitis': 128,
	u'/conditions/epidural-hemorrhage': 301,
	u'/conditions/epilepsy': 315,
	u'/conditions/erectile-dysfunction': 310,
	u'/conditions/erythema-multiforme': 2,
	u'/conditions/esophageal-cancer': 763,
	u'/conditions/esophageal-varices': 575,
	u'/conditions/esophagitis': 293,
	u'/conditions/essential-tremor': 59,
	u'/conditions/eustachian-tube-dysfunction-ear-disorder': 172,
	u'/conditions/extrapyramidal-effect-of-drugs': 387,
	u'/conditions/eye-alignment-disorder': 279,
	u'/conditions/factitious-disorder': 265,
	u'/conditions/fat-embolism': 503,
	u'/conditions/female-genitalia-infection': 89,
	u'/conditions/female-infertility-of-unknown-cause': 770,
	u'/conditions/fetal-alcohol-syndrome': 5,
	u'/conditions/fibroadenoma': 714,
	u'/conditions/fibrocystic-breast-disease': 115,
	u'/conditions/fibromyalgia': 708,
	u'/conditions/flat-feet': 260,
	u'/conditions/floaters': 44,
	u'/conditions/flu': 460,
	u'/conditions/fluid-overload': 722,
	u'/conditions/folate-deficiency': 70,
	u'/conditions/food-allergy': 74,
	u'/conditions/foreign-body-in-the-ear': 427,
	u'/conditions/foreign-body-in-the-eye': 525,
	u'/conditions/foreign-body-in-the-gastrointestinal-tract': 246,
	u'/conditions/foreign-body-in-the-nose': 247,
	u'/conditions/foreign-body-in-the-throat': 325,
	u'/conditions/foreign-body-in-the-vagina': 718,
	u'/conditions/fracture-of-the-ankle': 439,
	u'/conditions/fracture-of-the-arm': 174,
	u'/conditions/fracture-of-the-facial-bones': 702,
	u'/conditions/fracture-of-the-finger': 358,
	u'/conditions/fracture-of-the-foot': 205,
	u'/conditions/fracture-of-the-hand': 327,
	u'/conditions/fracture-of-the-jaw': 580,
	u'/conditions/fracture-of-the-leg': 492,
	u'/conditions/fracture-of-the-neck': 384,
	u'/conditions/fracture-of-the-patella': 13,
	u'/conditions/fracture-of-the-pelvis': 746,
	u'/conditions/fracture-of-the-rib': 114,
	u'/conditions/fracture-of-the-shoulder': 538,
	u'/conditions/fracture-of-the-skull': 449,
	u'/conditions/fracture-of-the-vertebra': 462,
	u'/conditions/friedrich-ataxia': 588,
	u'/conditions/frostbite': 71,
	u'/conditions/fungal-infection-of-the-hair': 20,
	u'/conditions/fungal-infection-of-the-skin': 465,
	u'/conditions/g6pd-enzyme-deficiency': 451,
	u'/conditions/galactorrhea-of-unknown-cause': 236,
	u'/conditions/gallbladder-cancer': 586,
	u'/conditions/gallbladder-disease': 791,
	u'/conditions/gallstone': 90,
	u'/conditions/ganglion-cyst': 3,
	u'/conditions/gas-gangrene': 224,
	u'/conditions/gastritis': 33,
	u'/conditions/gastroduodenal-ulcer': 190,
	u'/conditions/gastroesophageal-reflux-disease-gerd': 329,
	u'/conditions/gastrointestinal-hemorrhage': 576,
	u'/conditions/gastroparesis': 466,
	u'/conditions/genital-herpes': 560,
	u'/conditions/gestational-diabetes': 335,
	u'/conditions/glaucoma': 703,
	u'/conditions/glucocorticoid-deficiency': 788,
	u'/conditions/goiter': 436,
	u'/conditions/gonorrhea': 201,
	u'/conditions/gout': 96,
	u'/conditions/granuloma-inguinale': 423,
	u'/conditions/graves-disease': 405,
	u'/conditions/guillain-barre-syndrome': 234,
	u'/conditions/gum-disease': 155,
	u'/conditions/gynecomastia': 743,
	u'/conditions/hammer-toe': 415,
	u'/conditions/hashimoto-thyroiditis': 394,
	u'/conditions/head-and-neck-cancer': 60,
	u'/conditions/head-injury': 622,
	u'/conditions/headache-after-lumbar-puncture': 692,
	u'/conditions/heart-attack': 678,
	u'/conditions/heart-block': 118,
	u'/conditions/heart-contusion': 629,
	u'/conditions/heart-failure': 420,
	u'/conditions/heat-exhaustion': 352,
	u'/conditions/heat-stroke': 653,
	u'/conditions/hemangioma': 614,
	u'/conditions/hemarthrosis': 49,
	u'/conditions/hematoma': 630,
	u'/conditions/hemiplegia': 607,
	u'/conditions/hemochromatosis': 494,
	u'/conditions/hemolytic-anemia': 107,
	u'/conditions/hemophilia': 457,
	u'/conditions/hemorrhagic-fever': 604,
	u'/conditions/hemorrhoids': 161,
	u'/conditions/hepatic-encephalopathy': 210,
	u'/conditions/hepatitis-due-to-a-toxin': 727,
	u'/conditions/herniated-disk': 798,
	u'/conditions/herpangina': 355,
	u'/conditions/hiatal-hernia': 111,
	u'/conditions/hidradenitis-suppurativa': 218,
	u'/conditions/high-blood-pressure': 686,
	u'/conditions/hirschsprung-disease': 485,
	u'/conditions/hirsutism': 374,
	u'/conditions/histoplasmosis': 516,
	u'/conditions/hormone-disorder': 204,
	u'/conditions/hpv': 222,
	u'/conditions/human-immunodeficiency-virus-infection-hiv': 683,
	u'/conditions/huntington-disease': 434,
	u'/conditions/hydatidiform-mole': 442,
	u'/conditions/hydrocele-of-the-testicle': 72,
	u'/conditions/hydrocephalus': 767,
	u'/conditions/hydronephrosis': 298,
	u'/conditions/hypercalcemia': 609,
	u'/conditions/hypercholesterolemia': 486,
	u'/conditions/hyperemesis-gravidarum': 180,
	u'/conditions/hypergammaglobulinemia': 252,
	u'/conditions/hyperhidrosis': 573,
	u'/conditions/hyperkalemia': 626,
	u'/conditions/hyperlipidemia': 197,
	u'/conditions/hypernatremia': 169,
	u'/conditions/hyperopia': 24,
	u'/conditions/hyperosmotic-hyperketotic-state': 773,
	u'/conditions/hypertension-of-pregnancy': 635,
	u'/conditions/hypertensive-heart-disease': 598,
	u'/conditions/hypertrophic-obstructive-cardiomyopathy-hocm': 102,
	u'/conditions/hypocalcemia': 563,
	u'/conditions/hypoglycemia': 556,
	u'/conditions/hypokalemia': 338,
	u'/conditions/hyponatremia': 367,
	u'/conditions/hypospadias': 480,
	u'/conditions/hypothermia': 697,
	u'/conditions/hypothyroidism': 67,
	u'/conditions/hypovolemia': 120,
	u'/conditions/idiopathic-absence-of-menstruation': 217,
	u'/conditions/idiopathic-excessive-menstruation': 474,
	u'/conditions/idiopathic-infrequent-menstruation': 700,
	u'/conditions/idiopathic-irregular-menstrual-cycle': 332,
	u'/conditions/idiopathic-nonmenstrual-bleeding': 211,
	u'/conditions/idiopathic-painful-menstruation': 502,
	u'/conditions/ileus': 292,
	u'/conditions/impetigo': 95,
	u'/conditions/impulse-control-disorder': 313,
	u'/conditions/indigestion': 318,
	u'/conditions/induced-abortion': 694,
	u'/conditions/infection-of-open-wound': 101,
	u'/conditions/infectious-gastroenteritis': 747,
	u'/conditions/ingrown-toe-nail': 206,
	u'/conditions/inguinal-hernia': 668,
	u'/conditions/injury-of-the-ankle': 183,
	u'/conditions/injury-to-internal-organ': 309,
	u'/conditions/injury-to-the-abdomen': 472,
	u'/conditions/injury-to-the-arm': 623,
	u'/conditions/injury-to-the-face': 658,
	u'/conditions/injury-to-the-finger': 704,
	u'/conditions/injury-to-the-hand': 513,
	u'/conditions/injury-to-the-hip': 389,
	u'/conditions/injury-to-the-knee': 193,
	u'/conditions/injury-to-the-leg': 98,
	u'/conditions/injury-to-the-shoulder': 167,
	u'/conditions/injury-to-the-spinal-cord': 637,
	u'/conditions/injury-to-the-trunk': 159,
	u'/conditions/insect-bite': 787,
	u'/conditions/insulin-overdose': 368,
	u'/conditions/interstitial-lung-disease': 245,
	u'/conditions/intertrigo-skin-condition': 410,
	u'/conditions/intestinal-cancer': 77,
	u'/conditions/intestinal-disease': 546,
	u'/conditions/intestinal-malabsorption': 429,
	u'/conditions/intestinal-obstruction': 378,
	u'/conditions/intracerebral-hemorrhage': 64,
	u'/conditions/intracranial-abscess': 559,
	u'/conditions/intracranial-hemorrhage': 225,
	u'/conditions/intussusception': 212,
	u'/conditions/iridocyclitis': 715,
	u'/conditions/iron-deficiency-anemia': 404,
	u'/conditions/irritable-bowel-syndrome': 286,
	u'/conditions/ischemia-of-the-bowel': 484,
	u'/conditions/ischemic-heart-disease': 483,
	u'/conditions/itching-of-unknown-cause': 372,
	u'/conditions/jaw-disorder': 569,
	u'/conditions/joint-effusion': 124,
	u'/conditions/juvenile-rheumatoid-arthritis': 171,
	u'/conditions/kaposi-sarcoma': 750,
	u'/conditions/kidney-cancer': 126,
	u'/conditions/kidney-disease-due-to-longstanding-hypertension': 351,
	u'/conditions/kidney-failure': 99,
	u'/conditions/kidney-stone': 324,
	u'/conditions/knee-ligament-or-meniscus-tear': 652,
	u'/conditions/labyrinthitis': 30,
	u'/conditions/lactose-intolerance': 712,
	u'/conditions/laryngitis': 650,
	u'/conditions/lateral-epicondylitis-tennis-elbow': 446,
	u'/conditions/lead-poisoning': 277,
	u'/conditions/leishmaniasis': 784,
	u'/conditions/leptospirosis': 481,
	u'/conditions/leukemia': 435,
	u'/conditions/lewy-body-dementia': 39,
	u'/conditions/lice': 316,
	u'/conditions/lichen-planus': 527,
	u'/conditions/lichen-simplex': 7,
	u'/conditions/lipoma': 602,
	u'/conditions/liver-cancer': 258,
	u'/conditions/liver-disease': 360,
	u'/conditions/lumbago': 144,
	u'/conditions/lung-cancer': 796,
	u'/conditions/lung-contusion': 450,
	u'/conditions/lyme-disease': 615,
	u'/conditions/lymphadenitis': 346,
	u'/conditions/lymphangitis': 43,
	u'/conditions/lymphedema--2': 612,
	u'/conditions/lymphogranuloma-venereum': 507,
	u'/conditions/lymphoma': 690,
	u'/conditions/macular-degeneration': 539,
	u'/conditions/magnesium-deficiency': 365,
	u'/conditions/malaria': 227,
	u'/conditions/male-genitalia-infection': 606,
	u'/conditions/malignant-hypertension': 638,
	u'/conditions/marfan-syndrome': 216,
	u'/conditions/marijuana-abuse': 585,
	u'/conditions/mastectomy': 597,
	u'/conditions/mastoiditis': 0,
	u'/conditions/meckel-diverticulum': 317,
	u'/conditions/melanoma': 280,
	u'/conditions/meniere-disease': 80,
	u'/conditions/meningioma': 739,
	u'/conditions/meningitis': 337,
	u'/conditions/menopause': 4,
	u'/conditions/metabolic-disorder': 800,
	u'/conditions/metastatic-cancer': 262,
	u'/conditions/migraine': 797,
	u'/conditions/missed-abortion': 299,
	u'/conditions/mitral-valve-disease': 583,
	u'/conditions/mittelschmerz': 501,
	u'/conditions/molluscum-contagiosum': 561,
	u'/conditions/mononeuritis': 91,
	u'/conditions/mononucleosis': 696,
	u'/conditions/moyamoya-disease': 305,
	u'/conditions/mucositis': 92,
	u'/conditions/multiple-myeloma': 510,
	u'/conditions/multiple-sclerosis': 366,
	u'/conditions/mumps': 478,
	u'/conditions/muscle-spasm': 207,
	u'/conditions/muscular-dystrophy': 6,
	u'/conditions/myasthenia-gravis': 31,
	u'/conditions/myelodysplastic-syndrome': 181,
	u'/conditions/myocarditis': 257,
	u'/conditions/myoclonus': 320,
	u'/conditions/myopia': 66,
	u'/conditions/myositis': 409,
	u'/conditions/narcolepsy': 537,
	u'/conditions/nasal-polyp': 97,
	u'/conditions/necrotizing-fasciitis': 520,
	u'/conditions/neonatal-jaundice': 711,
	u'/conditions/nerve-impingement-near-the-shoulder': 46,
	u'/conditions/neuralgia': 136,
	u'/conditions/neurofibromatosis': 558,
	u'/conditions/neuromyelitis-optica': 240,
	u'/conditions/neuropathy-due-to-drugs': 339,
	u'/conditions/neurosis': 627,
	u'/conditions/nonalcoholic-liver-disease-nash': 647,
	u'/conditions/noninfectious-gastroenteritis': 396,
	u'/conditions/normal-pressure-hydrocephalus': 88,
	u'/conditions/nose-disorder': 757,
	u'/conditions/obesity': 657,
	u'/conditions/obsessive-compulsive-disorder-ocd': 592,
	u'/conditions/obstructive-sleep-apnea-osa': 347,
	u'/conditions/omphalitis': 783,
	u'/conditions/onychomycosis': 587,
	u'/conditions/open-wound-due-to-trauma': 701,
	u'/conditions/open-wound-from-surgical-incision': 55,
	u'/conditions/open-wound-of-the-abdomen': 25,
	u'/conditions/open-wound-of-the-arm': 618,
	u'/conditions/open-wound-of-the-back': 438,
	u'/conditions/open-wound-of-the-cheek': 676,
	u'/conditions/open-wound-of-the-chest': 584,
	u'/conditions/open-wound-of-the-ear': 173,
	u'/conditions/open-wound-of-the-eye': 749,
	u'/conditions/open-wound-of-the-face': 232,
	u'/conditions/open-wound-of-the-finger': 765,
	u'/conditions/open-wound-of-the-foot': 28,
	u'/conditions/open-wound-of-the-hand': 76,
	u'/conditions/open-wound-of-the-head': 617,
	u'/conditions/open-wound-of-the-hip': 754,
	u'/conditions/open-wound-of-the-jaw': 51,
	u'/conditions/open-wound-of-the-knee': 596,
	u'/conditions/open-wound-of-the-lip': 319,
	u'/conditions/open-wound-of-the-mouth': 523,
	u'/conditions/open-wound-of-the-neck': 32,
	u'/conditions/open-wound-of-the-nose': 656,
	u'/conditions/open-wound-of-the-shoulder': 776,
	u'/conditions/oppositional-disorder': 679,
	u'/conditions/optic-neuritis': 302,
	u'/conditions/oral-leukoplakia': 530,
	u'/conditions/oral-mucosal-lesion': 470,
	u'/conditions/oral-thrush-yeast-infection': 490,
	u'/conditions/orbital-cellulitis': 582,
	u'/conditions/orthostatic-hypotension': 717,
	u'/conditions/osteoarthritis': 489,
	u'/conditions/osteochondroma': 38,
	u'/conditions/osteochondrosis': 628,
	u'/conditions/osteomyelitis': 398,
	u'/conditions/osteoporosis': 214,
	u'/conditions/otitis-externa-swimmer-s-ear': 179,
	u'/conditions/otitis-media': 785,
	u'/conditions/otosclerosis': 276,
	u'/conditions/ovarian-cancer': 699,
	u'/conditions/ovarian-cyst': 548,
	u'/conditions/ovarian-torsion': 730,
	u'/conditions/overflow-incontinence': 479,
	u'/conditions/paget-disease': 517,
	u'/conditions/pain-after-an-operation': 406,
	u'/conditions/pain-disorder-affecting-the-neck': 456,
	u'/conditions/pancreatic-cancer': 113,
	u'/conditions/panic-attack': 543,
	u'/conditions/panic-disorder': 574,
	u'/conditions/parasitic-disease': 373,
	u'/conditions/parathyroid-adenoma': 570,
	u'/conditions/parkinson-disease': 648,
	u'/conditions/paronychia': 165,
	u'/conditions/paroxysmal-supraventricular-tachycardia': 552,
	u'/conditions/paroxysmal-ventricular-tachycardia': 375,
	u'/conditions/patau-syndrome': 684,
	u'/conditions/pelvic-fistula': 303,
	u'/conditions/pelvic-inflammatory-disease': 239,
	u'/conditions/pelvic-organ-prolapse': 168,
	u'/conditions/pemphigus': 707,
	u'/conditions/pericarditis': 388,
	u'/conditions/peripheral-arterial-disease': 454,
	u'/conditions/peripheral-arterial-embolism': 413,
	u'/conditions/peripheral-nerve-disorder': 364,
	u'/conditions/perirectal-infection': 191,
	u'/conditions/peritonitis': 661,
	u'/conditions/peritonsillar-abscess': 170,
	u'/conditions/persistent-vomiting-of-unknown-cause': 729,
	u'/conditions/personality-disorder': 353,
	u'/conditions/peyronie-disease': 642,
	u'/conditions/pharyngitis': 10,
	u'/conditions/phimosis': 8,
	u'/conditions/pick-disease': 62,
	u'/conditions/pilonidal-cyst': 283,
	u'/conditions/pinguecula': 473,
	u'/conditions/pinworm-infection': 540,
	u'/conditions/pituitary-adenoma': 455,
	u'/conditions/pituitary-disorder': 412,
	u'/conditions/pityriasis-rosea': 721,
	u'/conditions/placenta-previa': 36,
	u'/conditions/placental-abruption': 723,
	u'/conditions/plague': 487,
	u'/conditions/plantar-fasciitis': 672,
	u'/conditions/pleural-effusion': 300,
	u'/conditions/pneumoconiosis': 453,
	u'/conditions/pneumonia': 706,
	u'/conditions/pneumothorax': 156,
	u'/conditions/poisoning-due-to-analgesics': 328,
	u'/conditions/poisoning-due-to-anticonvulsants': 81,
	u'/conditions/poisoning-due-to-antidepressants': 662,
	u'/conditions/poisoning-due-to-antihypertensives': 496,
	u'/conditions/poisoning-due-to-antimicrobial-drugs': 83,
	u'/conditions/poisoning-due-to-antipsychotics': 440,
	u'/conditions/poisoning-due-to-ethylene-glycol': 779,
	u'/conditions/poisoning-due-to-gas': 84,
	u'/conditions/poisoning-due-to-opioids': 73,
	u'/conditions/poisoning-due-to-sedatives': 87,
	u'/conditions/polycystic-kidney-disease': 238,
	u'/conditions/polycystic-ovarian-syndrome-pcos': 407,
	u'/conditions/polycythemia-vera': 297,
	u'/conditions/polymyalgia-rheumatica': 498,
	u'/conditions/post-traumatic-stress-disorder-ptsd': 567,
	u'/conditions/postoperative-infection': 256,
	u'/conditions/postpartum-depression': 547,
	u'/conditions/preeclampsia': 748,
	u'/conditions/pregnancy': 665,
	u'/conditions/premature-atrial-contractions-pacs': 282,
	u'/conditions/premature-ovarian-failure': 223,
	u'/conditions/premature-rupture-of-amniotic-membrane': 54,
	u'/conditions/premature-ventricular-contractions-pvcs': 505,
	u'/conditions/premenstrual-tension-syndrome': 731,
	u'/conditions/presbyacusis': 395,
	u'/conditions/presbyopia': 52,
	u'/conditions/priapism': 56,
	u'/conditions/primary-immunodeficiency': 493,
	u'/conditions/primary-insomnia': 17,
	u'/conditions/primary-kidney-disease': 634,
	u'/conditions/primary-thrombocythemia': 645,
	u'/conditions/problem-during-pregnancy': 601,
	u'/conditions/prostate-cancer': 771,
	u'/conditions/prostatitis': 719,
	u'/conditions/protein-deficiency': 671,
	u'/conditions/pseudohypoparathyroidism': 314,
	u'/conditions/pseudotumor-cerebri': 359,
	u'/conditions/psoriasis': 12,
	u'/conditions/psychosexual-disorder': 786,
	u'/conditions/psychotic-disorder': 533,
	u'/conditions/pterygium': 380,
	u'/conditions/pulmonary-congestion': 295,
	u'/conditions/pulmonary-embolism': 564,
	u'/conditions/pulmonary-eosinophilia': 14,
	u'/conditions/pulmonary-fibrosis': 85,
	u'/conditions/pulmonary-hypertension': 154,
	u'/conditions/pulmonic-valve-disease': 500,
	u'/conditions/pyelonephritis': 669,
	u'/conditions/pyloric-stenosis': 177,
	u'/conditions/pyogenic-skin-infection': 447,
	u'/conditions/rabies': 321,
	u'/conditions/raynaud-disease': 176,
	u'/conditions/reactive-arthritis': 331,
	u'/conditions/rectal-disorder': 345,
	u'/conditions/restless-leg-syndrome': 199,
	u'/conditions/retinal-detachment': 357,
	u'/conditions/retinopathy-due-to-high-blood-pressure': 521,
	u'/conditions/rhabdomyolysis': 639,
	u'/conditions/rheumatic-fever': 41,
	u'/conditions/rheumatoid-arthritis': 536,
	u'/conditions/rocky-mountain-spotted-fever': 594,
	u'/conditions/rosacea': 22,
	u'/conditions/rotator-cuff-injury': 738,
	u'/conditions/salivary-gland-disorder': 390,
	u'/conditions/sarcoidosis': 511,
	u'/conditions/scabies': 15,
	u'/conditions/scar': 476,
	u'/conditions/scarlet-fever': 581,
	u'/conditions/schizophrenia': 464,
	u'/conditions/sciatica': 463,
	u'/conditions/scleritis': 272,
	u'/conditions/scleroderma': 720,
	u'/conditions/scoliosis': 551,
	u'/conditions/scurvy': 713,
	u'/conditions/seasonal-allergies-hay-fever': 675,
	u'/conditions/sebaceous-cyst': 529,
	u'/conditions/seborrheic-dermatitis': 354,
	u'/conditions/seborrheic-keratosis': 733,
	u'/conditions/sensorineural-hearing-loss': 506,
	u'/conditions/sepsis': 203,
	u'/conditions/septic-arthritis': 119,
	u'/conditions/shingles-herpes-zoster': 150,
	u'/conditions/sialoadenitis': 274,
	u'/conditions/sick-sinus-syndrome': 93,
	u'/conditions/sickle-cell-anemia': 158,
	u'/conditions/sickle-cell-crisis': 312,
	u'/conditions/sinus-bradycardia': 100,
	u'/conditions/sjogren-syndrome': 698,
	u'/conditions/skin-cancer': 125,
	u'/conditions/skin-disorder': 323,
	u'/conditions/skin-pigmentation-disorder': 166,
	u'/conditions/skin-polyp': 23,
	u'/conditions/smoking-or-tobacco-addiction': 418,
	u'/conditions/social-phobia': 237,
	u'/conditions/soft-tissue-sarcoma': 425,
	u'/conditions/somatization-disorder': 35,
	u'/conditions/spermatocele': 760,
	u'/conditions/spherocytosis': 571,
	u'/conditions/spina-bifida': 664,
	u'/conditions/spinal-stenosis': 795,
	u'/conditions/spinocerebellar-ataxia': 737,
	u'/conditions/spondylitis': 531,
	u'/conditions/spondylolisthesis': 781,
	u'/conditions/spondylosis': 735,
	u'/conditions/spontaneous-abortion': 467,
	u'/conditions/sporotrichosis': 376,
	u'/conditions/sprain-or-strain': 790,
	u'/conditions/stenosis-of-the-tear-duct': 751,
	u'/conditions/stomach-cancer': 195,
	u'/conditions/strep-throat': 379,
	u'/conditions/stress-incontinence': 403,
	u'/conditions/stricture-of-the-esophagus': 603,
	u'/conditions/stroke': 649,
	u'/conditions/stye': 562,
	u'/conditions/subacute-thyroiditis': 736,
	u'/conditions/subarachnoid-hemorrhage': 742,
	u'/conditions/subconjunctival-hemorrhage': 273,
	u'/conditions/subdural-hemorrhage': 666,
	u'/conditions/substance-related-mental-disorder': 591,
	u'/conditions/syndrome-of-inappropriate-secretion-of-adh-siadh': 356,
	u'/conditions/syphilis': 275,
	u'/conditions/syringomyelia': 680,
	u'/conditions/systemic-lupus-erythematosis-sle': 789,
	u'/conditions/teething-syndrome': 554,
	u'/conditions/temporary-or-benign-blood-in-urine': 68,
	u'/conditions/temporomandibular-joint-disorder': 775,
	u'/conditions/tendinitis': 235,
	u'/conditions/tension-headache': 230,
	u'/conditions/testicular-cancer': 362,
	u'/conditions/testicular-disorder': 691,
	u'/conditions/testicular-torsion': 611,
	u'/conditions/thalassemia': 605,
	u'/conditions/thoracic-aortic-aneurysm': 515,
	u'/conditions/thoracic-outlet-syndrome': 377,
	u'/conditions/threatened-pregnancy': 651,
	u'/conditions/thrombocytopenia': 146,
	u'/conditions/thrombophlebitis': 646,
	u'/conditions/thyroid-cancer': 134,
	u'/conditions/thyroid-disease': 208,
	u'/conditions/thyroid-nodule': 129,
	u'/conditions/tic-movement-disorder': 160,
	u'/conditions/tietze-syndrome': 549,
	u'/conditions/tinnitus-of-unknown-cause': 674,
	u'/conditions/tonsillar-hypertrophy': 518,
	u'/conditions/tonsillitis': 593,
	u'/conditions/tooth-abscess': 659,
	u'/conditions/tooth-disorder': 16,
	u'/conditions/torticollis': 542,
	u'/conditions/tourette-syndrome': 535,
	u'/conditions/toxic-multinodular-goiter': 522,
	u'/conditions/toxoplasmosis': 682,
	u'/conditions/tracheitis': 677,
	u'/conditions/transient-ischemic-attack': 370,
	u'/conditions/trichiasis': 185,
	u'/conditions/trichinosis': 774,
	u'/conditions/trichomonas-infection': 18,
	u'/conditions/tricuspid-valve-disease': 740,
	u'/conditions/trigeminal-neuralgia': 344,
	u'/conditions/trigger-finger-finger-disorder': 663,
	u'/conditions/tuberculosis': 688,
	u'/conditions/tuberous-sclerosis': 452,
	u'/conditions/turner-syndrome': 793,
	u'/conditions/typhoid-fever': 458,
	u'/conditions/ulcerative-colitis': 624,
	u'/conditions/urethral-disorder': 497,
	u'/conditions/urethral-stricture': 599,
	u'/conditions/urethral-valves': 290,
	u'/conditions/urethritis': 419,
	u'/conditions/urge-incontinence': 142,
	u'/conditions/urinary-tract-infection': 82,
	u'/conditions/urinary-tract-obstruction': 514,
	u'/conditions/uterine-atony': 499,
	u'/conditions/uterine-cancer': 132,
	u'/conditions/uterine-fibroids': 78,
	u'/conditions/uveitis': 655,
	u'/conditions/vacterl-syndrome': 621,
	u'/conditions/vaginal-cyst': 53,
	u'/conditions/vaginal-yeast-infection': 444,
	u'/conditions/vaginismus': 550,
	u'/conditions/vaginitis': 660,
	u'/conditions/valley-fever': 577,
	u'/conditions/varicocele-of-the-testicles': 400,
	u'/conditions/varicose-veins': 710,
	u'/conditions/vasculitis': 110,
	u'/conditions/venous-insufficiency': 414,
	u'/conditions/vertebrobasilar-insufficiency': 194,
	u'/conditions/vesicoureteral-reflux': 26,
	u'/conditions/viral-exanthem': 764,
	u'/conditions/viral-hepatitis': 363,
	u'/conditions/viral-warts': 411,
	u'/conditions/vitamin-a-deficiency': 198,
	u'/conditions/vitamin-b-deficiency': 248,
	u'/conditions/vitamin-b12-deficiency': 63,
	u'/conditions/vitamin-d-deficiency': 689,
	u'/conditions/vitreous-degeneration': 589,
	u'/conditions/vitreous-hemorrhage': 610,
	u'/conditions/vocal-cord-polyp': 544,
	u'/conditions/volvulus': 758,
	u'/conditions/von-hippel-lindau-disease': 741,
	u'/conditions/von-willebrand-disease': 799,
	u'/conditions/vulvar-cancer': 271,
	u'/conditions/vulvar-disorder': 461,
	u'/conditions/vulvodynia': 756,
	u'/conditions/wernicke-korsakoff-syndrome': 762,
	u'/conditions/west-nile-virus': 641,
	u'/conditions/white-blood-cell-disease': 745,
	u'/conditions/whooping-cough': 40,
	u'/conditions/wilson-disease': 631,
	u'/conditions/yeast-infection': 382,
	u'/conditions/zenker-diverticulum': 495
}

pickle.dump(a, open('symcat_to_remedy_id.p', 'wb'))

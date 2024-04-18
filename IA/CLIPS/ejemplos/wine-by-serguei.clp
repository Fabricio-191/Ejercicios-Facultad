;;
;; Serguei A. Mokhov <mokhov@cs.concordia.ca>
;; COMP474 - Assignment #3
;; Instructor: Sabine Bergler
;; Lab Instructor: Alina Andreevskaia
;; Ex. 5, p. 220 - Wine Adviser
;;

;;
;; README
;;
;; The program can be run in either 'clips' or
;; 'xclips' enviroment. It has been developed and
;; tested in the labs 962, 966, and 968  under UNIX (Solaris) 
;; and Linux (Red Hat) OSes.
;;
;; To execute the program one has to 
;;   o load it: (load "wine.clp")
;;   o reset to initial facts: (reset)
;;   o and finally run: (run)
;;
;; As soon as I was a little bit frustrated
;; while working on the program, some ouput messages
;; might sound too sarcastic. I appologize for this
;; in advance.
;;
;; There are about 16 wines in the system, some are real,
;; some are made up by me. The former wines are borrowed from
;; one clips file, with reference provided in the wine section.
;;
;; The program was designed to handle unusual cases
;; such as 'crocodile' or other dish/dish type, not
;; explicitly stated in the program.
;;
;; If more then one wine appear in the final list:
;;
;;   o for the wines with equal certainties
;;     program asks for preference and assignes
;;     the preferred the certainty of 1.0.
;;
;;   o for the wines with different certainties or
;;     the same certaties of 1.0 the program proposes
;;     the high-scorred one or the one on top.
;;
;; For the only wine, the program just proposes it.
;; If the user rejects everything, the program
;; gets very upset; and happy otherwise.
;;

;; CLIPS Wine Advisor,
;; after an OPS5 program by Rand Waltzman of Teknowledge
;; Choosing a wine to go with a meal,
;; based on properties of the dish and tastes of the diner


;; TEMPLATES

(deftemplate wine
  (field property (type SYMBOL))
  (field is (type SYMBOL))
  (field cert (type FLOAT))
)

(deftemplate meal 
  (field property (type SYMBOL))
  (field is (type SYMBOL))
)

(deftemplate decision
  (field re (type SYMBOL))
  (field is (type SYMBOL))
)


;; FACTS

(deffacts the-facts
  (task dish)
)


; Production rules of the form

; (defrule <rulename> <LHS> => <RHS>).

;; RULES THAT FIND OUT ABOUT THE DISH.

; This corresponds to the data abstraction stage.

; dish-type is the rule invoked first because its calling
; pattern is put into WM by the fact list when CLIPS is reset.

(defrule dish-type
  (initial-fact)
  (task dish)
=>
  (printout t crlf
			"Is the main dish of the meal MEAT, FISH or POULTRY?"
			t crlf
  )
  (assert (meal (property dish-type) (is (read))))
)

; meat finds out more about the dish, if it is meat.

(defrule meat
  (task dish)
  (meal (property dish-type) (is meat))
=>
  (printout	t crlf
			"What kind of meat? e.g. STEAK, VEAL, LAMB"
			t crlf
  )
  (assert (meal (property meat-type) (is (read))))
)


; You can write a similar rule for fish distinguishing, e.g.
; wet fish from shell fish; also a rule for poultry.

(defrule fish
  (task dish)
  (meal (property dish-type) (is fish))
=>
  (printout t crlf
			"What kind of fish? e.g. WET, SHELL, DRY"
			t crlf
  )
  (assert (meal (property fish-type) (is (read))))
)

(defrule poultry
  (task dish)
  (meal (property dish-type) (is poultry))
=>
  (printout t crlf
			"What kind of poultry? e.g. CHICKEN, DUCK, GOOSE, TURKEY"
			t crlf
  )
  (assert (meal (property poultry-type) (is (read))))
)


;; RULES THAT SUGGEST WINE PROPERTIES

; This is the heuristic matching stage.

; steak is an example of a meat rule which suggests wine properties.

(defrule steak
    ?task <- (task dish)
    (meal (property meat-type) (is steak))
    =>
    (assert (wine (property colour) (is red) (cert 1.0)))
    (assert (wine (property body) (is full) (cert 1.0)))
    (assert (wine (property flavour) (is dry) (cert 0.7)))
    (assert (wine (property flavour) (is sweet) (cert 0.2)))
    (retract ?task)
    (assert (task attributes))
)

; You can write similar rules for lamb, veal, etc.

(defrule lamb
    ?task <- (task dish)
    (meal (property meat-type) (is lamb))
    =>
    (assert (wine (property colour) (is red) (cert 1.0)))
    (assert (wine (property body) (is light) (cert 0.9)))
    (assert (wine (property flavour) (is sweet) (cert 0.75)))
    (assert (wine (property flavour) (is dry) (cert 0.3)))
    (retract ?task)
    (assert (task attributes))
)

(defrule veal
    ?task <- (task dish)
    (meal (property meat-type) (is veal))
    =>
    (assert (wine (property colour) (is rosee) (cert 0.85)))
    (assert (wine (property body) (is medium) (cert 1.0)))
    (assert (wine (property flavour) (is sweet) (cert 0.65)))
    (assert (wine (property flavour) (is dry) (cert 0.15)))
    (retract ?task)
    (assert (task attributes))
)

; We remove the dish task once we know what the dish is. 
; Then we set up the task of deciding upon wine attributes.

; Similar as the above but for fishes

(defrule wet-fish
    ?task <- (task dish)
    (meal (property fish-type) (is wet))
    =>
    (assert (wine (property colour) (is white) (cert 1.0)))
    (assert (wine (property body) (is light) (cert 0.9)))
    (assert (wine (property flavour) (is sweet) (cert 0.75)))
    (assert (wine (property flavour) (is dry) (cert 0.3)))
    (retract ?task)
    (assert (task attributes))
)

(defrule shell-fish
    ?task <- (task dish)
    (meal (property fish-type) (is shell))
    =>
    (assert (wine (property colour) (is white) (cert 1.0)))
    (assert (wine (property body) (is full) (cert 0.9)))
    (assert (wine (property flavour) (is dry) (cert 0.75)))
    (assert (wine (property flavour) (is sweet) (cert 0.3)))
    (retract ?task)
    (assert (task attributes))
)

(defrule dry-fish
    ?task <- (task dish)
    (meal (property fish-type) (is dry))
    =>
    (assert (wine (property colour) (is white) (cert 1.0)))
    (assert (wine (property body) (is medium) (cert 1.0)))
    (assert (wine (property flavour) (is dry) (cert 0.9)))
    (assert (wine (property flavour) (is sweet) (cert 0.1)))
    (retract ?task)
    (assert (task attributes))
)

; Similar as the above but for poultry

(defrule chicken
    ?task <- (task dish)
    (meal (property poultry-type) (is chicken))
    =>
    (assert (wine (property colour) (is red) (cert 0.8)))
    (assert (wine (property body) (is medium) (cert 1.0)))
    (assert (wine (property flavour) (is sweet) (cert 0.9)))
    (assert (wine (property flavour) (is dry) (cert 0.1)))
    (retract ?task)
    (assert (task attributes))
)

(defrule duck
    ?task <- (task dish)
    (meal (property poultry-type) (is duck))
    =>
    (assert (wine (property colour) (is rosee) (cert 1.0)))
    (assert (wine (property body) (is full) (cert 1.0)))
    (assert (wine (property flavour) (is dry) (cert 0.9)))
    (assert (wine (property flavour) (is sweet) (cert 0.1)))
    (retract ?task)
    (assert (task attributes))
)

(defrule goose
    ?task <- (task dish)
    (meal (property poultry-type) (is goose))
    =>
    (assert (wine (property colour) (is white) (cert 1.0)))
    (assert (wine (property body) (is medium) (cert 1.0)))
    (assert (wine (property flavour) (is dry) (cert 0.9)))
    (assert (wine (property flavour) (is sweet) (cert 0.1)))
    (retract ?task)
    (assert (task attributes))
)

(defrule turkey
    ?task <- (task dish)
    (meal (property poultry-type) (is turkey))
    =>
    (assert (wine (property colour) (is white) (cert 1.0)))
    (assert (wine (property body) (is medium) (cert 1.0)))
    (assert (wine (property flavour) (is dry) (cert 0.9)))
    (assert (wine (property flavour) (is sweet) (cert 0.1)))
    (retract ?task)
    (assert (task attributes))
)


; You should have default rules for meat, fish and poultry, which
; catch any cases, such as alligator, that you have not anticipated.

(defrule default-meat
    ?task <- (task dish)
    (not (meal (is steak)))
    (not (meal (is veal)))
    (not (meal (is lamb)))
    =>
    (assert (wine (property colour) (is red) (cert 0.5)))
    (assert (wine (property body) (is medium) (cert 0.5)))
    (assert (wine (property flavour) (is dry) (cert 0.5)))
    (assert (wine (property flavour) (is sweet) (cert 0.5)))
    (retract ?task)
    (assert (task attributes))
)

(defrule default-fish
    ?task <- (task dish)
    (not (meal (is wet)))
    (not (meal (is shell)))
    (not (meal (is dry)))
    =>
    (assert (wine (property colour) (is white) (cert 0.5)))
    (assert (wine (property body) (is medium) (cert 0.5)))
    (assert (wine (property flavour) (is dry) (cert 0.5)))
    (assert (wine (property flavour) (is sweet) (cert 0.5)))
    (retract ?task)
    (assert (task attributes))
)

(defrule default-poultry
    ?task <- (task dish)
    (not (meal (is chicken)))
    (not (meal (is turkey)))
    (not (meal (is goose)))
    (not (meal (is duck)))
    =>
    (assert (wine (property colour) (is red) (cert 0.5)))
    (assert (wine (property body) (is medium) (cert 0.5)))
    (assert (wine (property flavour) (is dry) (cert 0.5)))
    (assert (wine (property flavour) (is sweet) (cert 0.5)))
    (retract ?task)
    (assert (task attributes))
)


;; RULES THAT HANDLE CERTAINTIES

; If there are two structures in WM with the same value for
; the same attribute but with different certainties
; then attribute-update creates a third structure with a new value
; and deletes the other two.

; The formula for computing the new CF is
; 		cf = cf1 + cf2(1 - cf1)

(defrule attribute-update
    (task attributes)
    ?wine1 <- (wine (property ?attribute) (is ?value) (cert ?cert1))
    ?wine2 <- (wine (property ?attribute) (is ?value) (cert ?cert2))
    (test (<> ?cert1 ?cert2))
    => 
    (bind ?newcert (+ ?cert1 (* ?cert2 (- 1 ?cert1))))
    (assert (wine (property ?attribute) (is ?value) (cert ?newcert))) 
    (retract ?wine1)
    (retract ?wine2)
)


; Write a rule called preference, which is only invoked if there is 
; more than one possible value for an attribute in working memory.
; The rule should ask the user's preference and change the certainty 
; of the relevant attribute-value combination to unity, deleting the
; other values from working memory.

(defrule preference
  (task attributes)
  ?wine1 <- (wine (property ?attribute) (is ?value1) (cert ?cert1))
  ?wine2 <- (wine (property ?attribute) (is ?value2) (cert ?cert2))
  (test (<> (str-compare ?value1 ?value2) 0))
  (test (eq ?cert1 ?cert2))
=>
  (printout t crlf
			"Which " ?attribute " do you prefer ? (" ?value1 " or " ?value2 ")"
			t crlf
  )

  (bind ?preference-value (read))

  ; To check for input errors
  (bind ?input-error 0)

  (if (= (str-compare ?preference-value ?value1) 0)
	  then
	    (modify ?wine1 (cert 1.0) )
	  else
	    (if (= (str-compare ?preference-value ?value2) 0)
			then
			  (modify ?wine2 (cert 1.0) )
		    else
		      (printout t crlf "Please, select either " ?value1 " or " ?value2 "." t crlf)
			  (bind ?input-error 1)
	    )
  )

  ; Refire this rule again,
  ; to re-ask the preference
  (if (<> ?input-error 0)
	  then
	    (retract ?wine1)
		(retract ?wine2)
	    (assert (wine (property ?attribute) (is ?value1) (cert ?cert1)))
		(assert (wine (property ?attribute) (is ?value2) (cert ?cert2)))
  )
)


; Write a rule called choose-value which fires if there are two
; structures in working memory which carry different values
; under the same attribute.  The rule should choose the structure
; with the greater CF and delete the other.

(defrule choose-value
  (task attributes)
  ?wine1 <- (wine (property ?attribute) (is ?value1) (cert ?cert1))
  ?wine2 <- (wine (property ?attribute) (is ?value2) (cert ?cert2))
  (test (<> (str-compare ?value1 ?value2) 0))
  (test (<> ?cert1 ?cert2))
=>
  (if (< ?cert1 ?cert2)
	  then
	    (retract ?wine1)
	  else
	    (retract ?wine2)
  )
)


; Write a rule called unique, which fires if there is only one
; candidate value for an attribute, and declares the attribute done.

(defrule unique
  (task attributes)
  ?wine1 <- (wine (property ?attribute) (is ?value1) (cert ?cert1))
  ?wine2 <- (wine (property ?attribute) (is ?value2) (cert ?cert2))
  (test (= (str-compare ?value1 ?value2) 0))
=>
  (if (= (str-compare ?attribute body) 0)
	  then
	    (assert (body done))
      else
	    (if (= (str-compare ?attribute colour) 0)
			then
	 		  (assert (colour done))
			else
			  (if (= (str-compare ?attribute flavour) 0)
				  then
				    (assert (flavour done))
			  )
		)
  )
)


; Write a rule called unity, which fires if a particular value is
; definite (has CF = 1) and declares the attribute done.

(defrule unity
  (task attributes)
  ?wine1 <- (wine (property ?attribute) (is ?value1) (cert 1.0))
=>
  (if (= (str-compare ?attribute body) 0)
	  then
	    (assert (body done))
      else
	    (if (= (str-compare ?attribute colour) 0)
			then
	 		  (assert (colour done))
			else
			  (if (= (str-compare ?attribute flavour) 0)
				  then
				    (assert (flavour done))
			  )
		)
  )
)


; if all the attributes of the wine are done then report them

(defrule all-attributes-done
    ?task <- (task attributes)
    ?col <- (colour done)
    ?bod <- (body done)
    ?fla <- (flavour done)
    (wine (property colour) (is ?colour))
    (wine (property body) (is ?body))
    (wine (property flavour) (is ?flavour))
    => 
    (printout
	 t crlf
	 "Try a " ?flavour " " ?colour " wine with a " ?body " body"
	 t crlf
	)

    (retract ?col)
    (retract ?bod)
    (retract ?fla)

    (retract ?task)
    (assert (task brand))
)


; RULES FOR THE WINE

; Write a rule called go-choose which selects the highest scoring
; wine when no other rules will fire to propose any more wines.

(defrule go-choose
  ?task <- (task brand)
  ?wine1 <- (wine (property brand) (is ?brand-name1) (cert ?cert1))
  ?wine2 <- (wine (property brand) (is ?brand-name2) (cert ?cert2))

  ; In case we have only one wine, we should
  ; maintain this, so we don't retract the only
  ; wine brand from our working memory
  (test (<> (str-compare ?brand-name1 ?brand-name2) 0))
=>

  ; In case of the sam certanity,
  ; ask
  (if (eq ?cert1 ?cert2)
	  then
	    (printout t crlf
				  "Which brand do you prefer? " ?brand-name1 " or " ?brand-name2 "?"
				  t crlf
		)

		(bind ?response (read))

		(if (= (str-compare ?response ?brand-name1) 0)
			then
			  (bind ?cert1 1.0)
			else
			  (bind ?cert2 1.0)
		)
  )

  (if (> ?cert1 ?cert2)
	  then
	    (modify ?wine1 (cert ?cert1))
	  else
	    (modify ?wine2 (cert ?cert2))
  )

  (retract ?task)
  (assert (task selection))
)


; Select a wine, given an attribute-value description.
; This corresponds to the solution refinement stage.

(defrule refine
  ?task1 <- (task brand)
  ?wine1 <- (wine (property brand) (is ?brand-name1) (cert ?cert1))
  ?wine2 <- (wine (property brand) (is ?brand-name2) (cert ?cert2))
  (test (eq ?wine1 ?wine2))
=>
  (printout t crlf "Refining..." t crlf)
  (retract ?task1)
  (assert (task selection))
)


; Generate all the candidates before you offer selections to the user.

; soave is a sample wine rule.  Write as many as you like.

(defrule soave
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is white))
    (wine (property flavour) (is dry) (cert ?cert1))
    (wine (property body) (is fine) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is soave) (cert (min ?cert1 ?cert2))))
)


; These are adapted from:
; http://www.ghgcorp.com/clips/download/executables/examples/wine.clp
; and appear to be realistic :)

(defrule gamay
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is red))
    (wine (property flavour) (is sweet) (cert ?cert1))
    (wine (property body) (is medium) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is gamay) (cert (min ?cert1 ?cert2))))
)

(defrule chablis
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is white))
    (wine (property flavour) (is dry) (cert ?cert1))
    (wine (property body) (is light) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is chablis) (cert (min ?cert1 ?cert2))))
)

(defrule sauvignon-blanc
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is white))
    (wine (property flavour) (is dry) (cert ?cert1))
    (wine (property body) (is medium) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is sauvignon-blanc) (cert (min ?cert1 ?cert2))))
)

(defrule chardonnay
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is white))
    (wine (property flavour) (is medium-dry) (cert ?cert1))
    (wine (property body) (is medium-full) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is chardonnay) (cert (min ?cert1 ?cert2))))
)

(defrule riesling
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is white))
    (wine (property flavour) (is sweet) (cert ?cert1))
    (wine (property body) (is light) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is riesling) (cert (min ?cert1 ?cert2))))
)

(defrule geverztraminer
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is white))
    (wine (property body) (is full) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is geverztraminer) (cert ?cert2)))
)

(defrule chenin-blanc
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is white))
    (wine (property flavour) (is sweet) (cert ?cert1))
    (wine (property body) (is light) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is chenin-blanc) (cert (min ?cert1 ?cert2))))
)

(defrule valpolicella
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is red))
    (wine (property body) (is light) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is valpolicella) (cert ?cert2)))
)

(defrule cabernet-sauvignon
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is red))
    (wine (property flavour) (is dry) (cert ?cert1))
    (wine (property body) (is light) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is cabernet-sauvignon) (cert (min ?cert1 ?cert2))))
)

(defrule zinfandel
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is red))
    (wine (property flavour) (is dry-medium) (cert ?cert1))
    => 
    (assert
	(wine (property brand) (is zinfandel) (cert ?cert1)))
)

(defrule pinot-noir
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is red))
    (wine (property flavour) (is medium) (cert ?cert1))
    (wine (property body) (is medium) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is pinot-noir) (cert (min ?cert1 ?cert2))))
)

(defrule burgundy
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is red))
    (wine (property body) (is full) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is burgundy) (cert ?cert2)))
)


; My own, made up wines

(defrule roselina
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is rosee))
    (wine (property flavour) (is sweet) (cert ?cert1))
    (wine (property body) (is medium) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is roselina) (cert (min ?cert1 ?cert2))))
)

(defrule crocodile-special
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is white))
    (wine (property flavour) (is dry) (cert ?cert1))
    (wine (property body) (is medium) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is crocodile-special) (cert (min ?cert1 ?cert2))))
)

(defrule bizzarrino
    (declare (salience 1))
    (task brand)
    (wine (property colour) (is red))
    (wine (property flavour) (is medium) (cert ?cert1))
    (wine (property body) (is full) (cert ?cert2))
    => 
    (assert
	(wine (property brand) (is bizzarrino) (cert (min ?cert1 ?cert2))))
)


; RULES FOR PRESENTING SELECTIONS

; The user responds to these by typing 'yes' or 'no'.

; Write a rule called selection which finds the highest scoring wine
; and offers it to the user.

(defrule selection
  ?task <- (task selection)
  ?wine1 <- (wine (property brand) (is ?brand-name1) (cert ?cert1))
=>
  (printout t crlf
			"Would you please finally digest " ?brand-name1 "? (yes, no)"
			t crlf 
  )
  
  (assert (decision (re ?brand-name1) (is (read))))

  (retract ?task)
  (assert (task choice))
)


; In case nothing is matching
; we suggest some....

(defrule handle-no-brand-match
  ?task <- (task brand)
  (not (wine (property brand)))
  (meal (property dish-type) (is ?dish-type))
=>
  (printout t crlf
			"Unfortunately, even our wide collection of wines" t crlf
			"does not match your food preferences. However, may we" t crlf
			"suggest you something from our collection for your " ?dish-type "..." t crlf
  )

  (retract ?task)

  (if (= (str-compare ?dish-type fish) 0)
	  then
	    ; Just assert first three white wines
	    ; for any fish-like food.
	    (assert (wine (property brand) (is soave) (cert 1.0)))
	    (assert (wine (property brand) (is chablis) (cert 0.8)))
	    (assert (wine (property brand) (is sauvignon-blanc) (cert 0.6)))

	  else
	    ; Red wines for meat
	    (if (= (str-compare ?dish-type meat) 0)
			then
			  (assert (wine (property brand) (is gamay) (cert 1.0)))
			  (assert (wine (property brand) (is valpolicella) (cert 0.8)))
			  (assert (wine (property brand) (is burgundy) (cert 0.6)))
			else
	          ; Red and white wines for poultries
			  (if (= (str-compare ?dish-type poultry) 0)
				  then
				    (assert (wine (property brand) (is pinot-noir) (cert 1.0)))
				    (assert (wine (property brand) (is chenin-blanc) (cert 0.8)))
				    (assert (wine (property brand) (is zinfandel) (cert 0.6)))
				  else
				    ; "Exotic" dishes...
				    (assert (wine (property brand) (is crocodile-special) (cert 1.0)))
				    (assert (wine (property brand) (is roselina) (cert 0.8)))
				    (assert (wine (property brand) (is bizzarrino) (cert 0.6)))
		      )
		)
  )

  (assert (task brand))
)


; Write a rule called rejection which deals with a negative response
; to the current suggestion.

(defrule rejection
  ?task <- (task choice)
  (decision (re ?candidate) (is no))
  ?wine <- (wine (property brand) (is ?candidate))
=> 
  (printout t crlf
			"Sir/Madam has rejected " ?candidate "." t crlf
			"Proposing other remaining selections (if any)..."
			t crlf
  )

  (retract ?wine)
  (retract ?task)

  (assert (task selection))
)


; acceptance ends the session on the correct obsequious note.

(defrule acceptance
    (task choice)
    (decision (re ?candidate) (is yes))
    => 
    (printout t crlf 
			  "Sir/Madam has impeccable taste!" t crlf
			  "I'm a happy expert system now :)" t crlf
	)

	(facts)
    (halt)
)


; a very picky client will drink water!

(defrule end-of-the-world
=>
  (printout t crlf 
			"No more selections to offer :(" t crlf
			"Sir/Madam has auwful taste!!!" t crlf
			"Not able to choose anything at all!!!" t crlf
			"Shame on them!!!" t crlf
			"I'm so unhappy, so I terminate noe :(" t crlf
  )
  (facts)
  (halt)
)

; EOF

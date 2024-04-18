;;------------------------------ TEMPLATES ---------------------------------

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

    ;;-------------------------------- FACTS ------------------------------------

    (deffacts the-facts
      (task dish)
    )

    ;;-------------------------------- RULES ------------------------------------

    ; Production rules of the form

    ; (defrule <rulename> <LHS> => <RHS>).

    ;;==================== RULES THAT FIND OUT ABOUT THE DISH ====================

    ; This corresponds to the data abstraction stage.

    ; dish-type is the rule invoked first because its calling
    ; pattern is put into WM by the fact list when CLIPS is reset.

    (defrule dish-type
       (initial-fact)
       (task dish)
        => 
       (printout
            t crlf
            "Is the main dish of the meal MEAT, FISH or POULTRY?"
            t crlf)
       (assert (meal (property dish-type) (is (read))))
    )

    ;-----------------------------------------------------------------------
    ;; Checks if the user entered one of the three dish types. If not, the
    ;; program starts over.
    ;-----------------------------------------------------------------------
    (defrule not-dish-type
       ?task<-(task dish)
       (meal (property dish-type) (is ?dish))
       (test (<> (str-compare ?dish meat) 0))
       (test (<> (str-compare ?dish fish) 0))
       (test (<> (str-compare ?dish poultry) 0))
       =>
       (printout t crlf "You must enter MEAT, FISH or POULTRY." crlf)
       (retract ?task)
       (assert (task ask-user))
    )

    ;----------------------------------------------------------------------
    ; find out more about the type of MEAT DISH 

    (defrule meat
       (task dish)
       (meal (property dish-type) (is meat))
        => 
       (printout
            t crlf  
            "What kind of meat? e.g. STEAK, VEAL, LAMB."
            t crlf)
       (assert (meal (property meat-type) (is (read))))
    )


    ; You can write a similar rule for fish distinguishing, e.g.
    ; wet fish from shell fish; also a rule for poultry.

    ;--------------------------------------------------------------------
    ;; Find out more about the type of FISH DISH
    ;--------------------------------------------------------------------
    (defrule fish
       (task dish)
       (meal (property dish-type) (is fish))
       =>
       (printout 
            t crlf
            "What kind of fish? e.g. WET, SHELL, OILY."
            t crlf)
       (assert (meal (property fish-type) (is (read))))
    )

    ;--------------------------------------------------------------------
    ;; Find out more about the type of POULTRY DISH
    ;--------------------------------------------------------------------
    (defrule poultry
       (task dish)
       (meal (property dish-type) (is poultry))
       =>
       (printout
            t crlf
            "What kind of chicken? e.g. CHICKEN, TURKEY, DUCK."
            t crlf)
       (assert (meal (property poultry-type) (is (read))))
    )


    ;;====================== RULES THAT SUGGEST WINE PROPERTIES ===================

    ; This is the heuristic matching stage.

    ; steak is an example of a meat rule which suggests wine properties.

    ;----------------------------- STEAK

    (defrule steak
        ?task <- (task dish)
        (meal (property meat-type) (is steak))
        => 
        (assert (wine (property colour) (is red) (cert 1.0)))
        (assert (wine (property body) (is full) (cert 0.9)))
        (assert (wine (property flavour) (is dry) (cert 0.7)))
        (assert (wine (property flavour) (is sweet) (cert 0.2)))
        (retract ?task)
        (assert (task attributes))
    )

    ; You can write similar rules for lamb, veal, etc.
    ; We remove the dish task once we know what the dish is. 
    ; Then we set up the task of deciding upon wine attributes.

    ;----------------------------- LAMB

    (defrule lamb
        ?task <- (task dish)
        (meal (property meat-type) (is lamb))
        =>
        (assert (wine (property colour) (is red) (cert 0.8)))
        (assert (wine (property body) (is fine) (cert 0.5)))
        (assert (wine (property body) (is full) (cert 0.5)))
        (assert (wine (property flavour) (is dry) (cert 0.8)))
        (assert (wine (property flavour) (is sweet) (cert 0.1)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- VEAL

    (defrule veal
        ?task <- (task dish)
        (meal (property meat-type) (is veal))
        =>
        (assert (wine (property colour) (is white) (cert 0.7)))
        (assert (wine (property colour) (is red) (cert 0.7)))
        (assert (wine (property body) (is fine) (cert 1.0)))
        (assert (wine (property flavour) (is dry) (cert 0.5)))
        (assert (wine (property flavour) (is sweet) (cert 0.5)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- DEFAULT MEAT-TYPE

    (defrule meat-default
        ?task <- (task dish)
        (not (meal (property meat-type) (is steak)))
        (not (meal (property meat-type) (is veal)))
        (not (meal (property meat-type) (is lamb)))
        =>
        (assert (wine (property colour) (is red) (cert 0.7)))
        (assert (wine (property body) (is full) (cert 0.6)))
        (assert (wine (property flavour) (is sweet) (cert 0.8)))
        (assert (wine (property flavour) (is sweet) (cert 0.1)))
        (retract ?task)
        (assert (task attributes))
    )

    ; You should have default rules for meat, fish and poultry, which
    ; catch any cases, such as alligator, that you have not anticipated.

    ;----------------------------- WET-FISH

    (defrule wet-fish
        ?task <- (task dish)
        (meal (property fish-type) (is wet))
        =>
        (assert (wine (property colour) (is white) (cert 1.0)))
        (assert (wine (property colour) (is white) (cert 0.5)))
        (assert (wine (property body) (is fine) (cert 0.8)))
        (assert (wine (property flavour) (is dry) (cert 0.7)))
        (assert (wine (property flavour) (is sweet) (cert 0.1)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- SHELL-FISH

    (defrule shell-fish
        ?task <- (task dish)
        (meal (property fish-type) (is shell))
        =>
        (assert (wine (property colour) (is white) (cert 0.7)))
        (assert (wine (property body) (is fine) (cert 0.9)))
        (assert (wine (property flavour) (is dry) (cert 0.7)))
        (assert (wine (property flavour) (is sweet) (cert 0.1)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- OILY-FISH

    (defrule oily-fish
        ?task <- (task dish)
        (meal (property fish-type) (is oily))
        =>
        (assert (wine (property colour) (is red) (cert 1.0)))
        (assert (wine (property body) (is fine) (cert 1.0)))
        (assert (wine (property flavour) (is dry) (cert 0.6)))
        (assert (wine (property flavour) (is sweet) (cert 0.4)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- DEFAULT FISH-TYPE

    (defrule fish-default
        ?task <- (task dish)
        (not (meal (property meat-type) (is wet)))
        (not (meal (property meat-type) (is shell)))
        (not (meal (property meat-type) (is oily)))
        =>
        (assert (wine (property colour) (is white) (cert 0.7)))
        (assert (wine (property body) (is fine) (cert 0.8)))
        (assert (wine (property flavour) (is dry) (cert 0.5)))
        (assert (wine (property flavour) (is sweet) (cert 0.5)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- CHICKEN

    (defrule chicken
        ?task <- (task dish)
        (meal (property poultry-type) (is chicken))
        =>
        (assert (wine (property colour) (is white) (cert 1.0)))
        (assert (wine (property body) (is fine) (cert 0.7)))
         (assert (wine (property flavour) (is sweet) (cert 1.0)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- TURKEY

    (defrule turkey
        ?task <- (task dish)
        (meal (property poultry-type) (is turkey))
        =>
        (assert (wine (property colour) (is white) (cert 0.8)))
        (assert (wine (property body) (is fine) (cert 0.8)))
        (assert (wine (property flavour) (is dry) (cert 0.9)))
        (assert (wine (property flavour) (is sweet) (cert 0.2)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- DUCK

    (defrule duck
        ?task <- (task dish)
        (meal (property poultry-type) (is duck))
        =>
        (assert (wine (property colour) (is red) (cert 1.0)))
        (assert (wine (property body) (is full) (cert 0.9)))
        (assert (wine (property body) (is fine) (cert 0.9)))
        (assert (wine (property flavour) (is dry) (cert 0.6)))
        (assert (wine (property flavour) (is sweet) (cert 0.3)))
        (retract ?task)
        (assert (task attributes))
    )

    ;----------------------------- DEFAULT POULTRY-TYPE

    (defrule poultry-default
        ?task <- (task dish)
        (not (meal (property meat-type) (is chicken)))
        (not (meal (property meat-type) (is turkey)))
        (not (meal (property meat-type) (is duck)))
        =>
        (assert (wine (property colour) (is white) (cert 0.9)))
        (assert (wine (property body) (is fine) (cert 0.8)))
        (assert (wine (property flavour) (is dry) (cert 0.6)))
        (assert (wine (property flavour) (is sweet) (cert 0.4)))
        (retract ?task)
        (assert (task attributes))
    )

    ;;===================== RULES THAT HANDLE CERTAINTIES =========================

    ; If there are two structures in WM with the same value for
    ; the same attribute but with different certainties
    ; then attribute-update creates a third structure with a new value
    ; and deletes the other two.

    ; The formula for computing the new CF is
    ;               cf = cf1 + cf2(1 - cf1)

    ;; ATTRIBUTE-UPDATE
    ;;----------------------------------------------------------------------------
    ;; This rule was modified in case one of the certainties is 1.0. 
    ;; If that is the case, the old rule would retract both wine1 and wine2
    ;; and not replace them with a new fact. The reason is the new certainy 
    ;; will be 1.0 and the new fact to be asserted is already in the fact list.
    ;; The new rule will only retract one of them if the other has 1.0.
    ;;----------------------------------------------------------------------------
    (defrule attribute-update
        (task attributes)
        ?wine1 <- (wine (property ?attribute) (is ?value) (cert ?cert1))
        ?wine2 <- (wine (property ?attribute) (is ?value) (cert ?cert2))
        (test (<> ?cert1 ?cert2))
        => 
        (if (eq ?cert1 1.0)
            then (retract ?wine2)
        else (if (eq ?cert2 1.0)
            then (retract ?wine1)
        else  
            (bind ?newcert (+ ?cert1 (* ?cert2 (- 1 ?cert1))))
            (assert (wine (property ?attribute) (is ?value) (cert ?newcert)))
            (retract ?wine1)
            (retract ?wine2)))
    )

    ; Write a rule called preference, which is only invoked if there is 
    ; more than one possible value for an attribute in working memory.
    ; The rule should ask the user's preference and change the certainty 
    ; of the relevant attribute-value combination to unity, deleting the
    ; other values from working memory.

    ;; PREFERENCE
    ;------------------------------------------------------------------------
    ;; This rule looks for two wine facts with the same property attribute,
    ;; two different attribute values and the same certainties.
    ;; e.g. (wine (property flavour) (is dry) (cert 0.5))
    ;;      (wine (property flavour) (is sweet) (cert 0.5))
    ;------------------------------------------------------------------------
    (defrule preference
       (task attributes)
        ?wine1 <- (wine (property ?attribute) (is ?value1) (cert ?cert))
        ?wine2 <- (wine (property ?attribute) (is ?value2) (cert ?cert))
        (test (<> (str-compare ?value1 ?value2) 0))
        => 
        (printout 
            t crlf
            "wine with " ?attribute " " ?value1 " and certainty " ?cert crlf
            "wine with " ?attribute " " ?value2 " and certainty " ?cert crlf
            crlf "which do you prefer? " ?value1 " or " ?value2 "?"
            t crlf)
        (bind ?value (read))
        (if (eq (str-compare ?value ?value1) 0)
            then (modify ?wine1 (cert 1.0))
                 (retract ?wine2))
        (if (eq (str-compare ?value ?value2) 0)
            then (modify ?wine2 (cert 1.0))
                 (retract ?wine1))  
    )

    ; Write a rule called choose-value which fires if there are two
    ; structures in working memory which carry different values
    ; under the same attribute.  The rule should choose the structure
    ; with the greater CF and delete the other.

    ;; CHOOSE-VALUE
    ;------------------------------------------------------------------------
    ;; This rule looks for two wine facts with the same property attribute, 
    ;; two different attribute values and two different certainties.
    ;; e.g. (wine (property flavour) (is dry) (cert 0.8))
    ;;      (wine (property flavour) (is sweet) (cert 0.5))
    ;------------------------------------------------------------------------
    (defrule choose-value
       (task attributes)
        ?wine1 <- (wine (property ?attribute) (is ?value1) (cert ?cert1))
        ?wine2 <- (wine (property ?attribute) (is ?value2) (cert ?cert2))
        (test (<> ?cert1 ?cert2))
        => 
        (if (> ?cert1 ?cert2)
            then (retract ?wine2)
        else
            (retract ?wine1)) 
    )
    ;------------------------------------------------------------------------

    ; Write a rule called unique, which fires if there is only one
    ; candidate value for an attribute, and declares the attribute done.

    ;; UNIQUE
    (defrule unique
      (task attributes)
      ?wine1 <- (wine (property ?attribute) (is ?value1)(cert ?cert1))
      ?wine2 <- (wine (property ?attribute) (is ?value2) (cert ?cert2))  
      (test (eq (str-compare ?value1 ?value2) 0))
      =>
      (if (eq (str-compare ?attribute colour) 0)
            then (assert (colour done))
      else (if (eq (str-compare ?attribute body) 0)
            then (assert (body done)))
      else (if (eq (str-compare ?attribute flavour) 0)
            then (assert (flavour done))))
    )

    ;-----------------------------------------------------------------------

    ; Write a rule called unity, which fires if a particular value is
    ; definite (has CF = 1) and declares the attribute done.

    ;; UNITY
    (defrule unity
      (task attributes)
      (wine (property ?attribute) (is ?value)(cert ?cert))
      (test (eq ?cert 1.0))
      =>
      (if (eq (str-compare ?attribute colour) 0)
            then (assert (colour done))
      else (if (eq (str-compare ?attribute body) 0)
            then (assert (body done))
      else (if (eq (str-compare ?attribute flavour) 0)
            then (assert (flavour done)))))
    )

    ;------------------------------------------------------------------------
    ; if all the attributes of the wine are done then report them

    ;; ALL-ATTRIBUTES-DONE
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
            t crlf)
        (retract ?col)
        (retract ?bod)
        (retract ?fla)
        (retract ?task)
        (assert (task brand))
    )

    ;============================ RULES FOR THE WINE =============================

    ; Select a wine, given an attribute-value description.
    ; This corresponds to the solution refinement stage.
    ; Generate all the candidates before you offer selections to the user.

    ; soave is a sample wine rule.  Write as many as you like.

    (defrule soave
        (task brand)
        (wine (property colour) (is white))
        (wine (property flavour) (is dry) (cert ?cert1))
        (wine (property body) (is fine) (cert ?cert2))
        => 
        (assert
            (wine (property brand) (is soave) (cert (min ?cert1 ?cert2))))
    )

    (defrule zinfandel
       (task brand)
       (wine (property colour) (is red))
       (wine (property flavour) (is dry) (cert ?cert1))
       (wine (property body) (is fine) (cert ?cert2))
       =>
       (assert
            (wine (property brand) (is zinfandel) (cert (min ?cert1 ?cert2))))
    )

    (defrule chardonnay
       (task brand)
       (wine (property colour) (is white))
       (wine (property flavour) (is dry) (cert ?cert1))
       (wine (property body) (is full) (cert ?cert2))
       =>
       (assert
            (wine (property brand) (is chardonnay) (cert (min ?cert1 ?cert2))))
    )

    (defrule gamay
       (task brand)
       (wine (property colour) (is red))
       (wine (property flavour) (is sweet) (cert ?cert1))
       (wine (property body) (is full) (cert ?cert2))
       =>
       (assert
            (wine (property brand) (is gamay) (cert (min ?cert1 ?cert2))))
    )

    (defrule chablis
       (task brand)
       (wine (property colour) (is white))
       (wine (property flavour) (is dry) (cert ?cert1))
       (wine (property body) (is fine) (cert ?cert2))
       =>
       (assert
            (wine (property brand) (is chablis) (cert (min ?cert1 ?cert2))))
    )

    (defrule chenin-blanc
       (task brand)
       (wine (property colour) (is white))
       (wine (property flavour) (is sweet) (cert ?cert1))
       (wine (property body) (is fine) (cert ?cert2))
       =>
       (assert
            (wine (property brand) (is chenin-blanc) (cert (min ?cert1 ?cert2))))
    )

    (defrule riesling
       (task brand)
       (wine (property colour) (is white))
       (wine (property flavour) (is sweet) (cert ?cert1))
       (wine (property body) (is full) (cert ?cert2))
       =>
       (assert
            (wine (property brand) (is riesling) (cert (min ?cert1 ?cert2))))
    )
     
    (defrule pinot-noir
       (task brand)
       (wine (property colour) (is red))
       (wine (property flavour) (is sweet) (cert ?cert1))
       (wine (property body) (is full) (cert ?cert2))
       =>
       (assert
            (wine (property brand) (is pinot-noir) (cert (min ?cert1 ?cert2))))
    )

    (defrule burgundy
       (task brand)
       (wine (property colour) (is red))
       (wine (property flavour) (is sweet) (cert ?cert1))
       (wine (property body) (is full) (cert ?cert2))
       =>
       (assert
            (wine (property brand) (is burgundy) (cert (min ?cert1 ?cert2))))
    )

    ;; PRINT-WINE-BRAND
    ;------------------------------------------------------------------------------
    ;; The program ends here when one of the wine rules fire
    ;------------------------------------------------------------------------------
    (defrule print-wine-brand
       ?task<-(task brand)
       (wine (property brand) (is ?brand-name) (cert ?cert))
       =>
       (printout t crlf "We recommend " ?brand-name " with certainty " ?cert crlf)
       (retract ?task)
       (assert (task ask-user))
    )

    ; Write a rule called go-choose which selects the highest scoring
    ; wine when no other rules will fire to propose any more wines.

    ;; GO-CHOOSE
    ;------------------------------------------------------------------------------
    ;; Assumption 1 for go-choose:
    ;; This rule fires when at least two wine rules fire, i.e., two different
    ;; brands with the same certainties. The selection rule will follow.
    ;------------------------------------------------------------------------------
    (defrule go-choose
       ?task<-(task brand)
       (wine (property brand) (is ?brand-name1) (cert ?cert))
       (wine (property brand) (is ?brand-name2) (cert ?cert))
       (test (<> (str-compare ?brand-name1 ?brand-name2) 0))
       =>
       (retract ?task)
       (assert (task choose-brand))
       (printout t crlf "We recommend the following brands..." crlf)
    )

    ;; DEFAULT-GO-CHOOSE
    ;------------------------------------------------------------------------------
    ;; Assumption 2 for go-choose:
    ;; This rule fires when none of the wine rules fire.
    ;; Depending on the dish type, it assert 3 wine facts presented with decreasing
    ;; certainty. The selection rule will follow.
    ;------------------------------------------------------------------------------
    (defrule default-go-choose
       ?task<-(task brand)
       (not (wine (property brand) (is ?brand-name) (cert ?cert)))
       (meal (property dish-type) (is ?type))
       =>
       (if (eq (str-compare ?type meat) 0)
           then 
              (assert (wine (property brand) (is pinot-noir) (cert 0.6)))
              (assert (wine (property brand) (is gamay) (cert 0.8)))
              (assert (wine (property brand) (is zinfandel) (cert 1.0))))

       (if (eq (str-compare ?type fish) 0)
           then 
              (assert (wine (property brand) (is burgundy) (cert 0.5)))
              (assert (wine (property brand) (is chardonnay) (cert 0.6)))
              (assert (wine (property brand) (is soave) (cert 0.9))))

       (if (eq (str-compare ?type poultry) 0)
           then 
              (assert (wine (property brand) (is chablis) (cert 0.4)))
              (assert (wine (property brand) (is riesling) (cert 0.7)))
              (assert (wine (property brand) (is chenin-blanc) (cert 0.9))))

       (printout t crlf "We have no brands that match your preference." crlf
                        "However, we recommend 3 brands..." t crlf)
       (assert (task choose-brand))
       (retract ?task)
    )

    ;====================== RULES FOR PRESENTING SELECTIONS ======================

    ; The user responds to these by typing 'yes' or 'no'.

    ; Write a rule called selection which finds the highest scoring wine
    ; and offers it to the user.

    ;; SELECTION
    ;------------------------------------------------------------------------------
    ;; Assupmtion for selection rule:
    ;; This rule follows from the results of the go-choose or the default-go-choose
    ;; rules. It will offer the user each brand for every wine in the fact list.
    ;; The rule will stop after the user has made a selection or there are no
    ;; selections left. If the user responds 'yes' then acceptance rule will fire 
    ;; next. If the user responds 'no' then selection or the rejection rule will
    ;; fire next.
    ;------------------------------------------------------------------------------
    (defrule selection
       ?task<-(task choose-brand)
       ?wine<-(wine (property brand) (is ?brand-name) (cert ?cert))
       =>
       (printout t crlf 
                 "Would you like " ?brand-name " with certainty " ?cert ", yes/no" 
    crlf)
       (bind ?ans (read))
       (if (eq (str-compare ?ans yes) 0)
            then 
               (retract ?task)
               (assert (task choice))
               (assert (decision (re ?brand-name) (is yes)))
       else 
       (if (eq (str-compare ?ans no) 0)
           then 
               (retract ?wine)))
    )

    ; Write a rule called rejection which deals with a negative response
    ; to the current suggestion.

    ;; REJECTION
    ;------------------------------------------------------------------------------
    ;; Assupmtion for rejection rule:
    ;; This follows from the the selection rule. So the program ends here when
    ;; there are no wine facts left and comments on the user's selection.
    ;------------------------------------------------------------------------------
    (defrule rejection
       ?task<-(task choose-brand)
       (not (wine (property brand) (is ?brand-name) (cert ?cert)))
       =>
       (printout t crlf "There are no more selections." crlf
                        "Sir/Madame will have to drink water!" crlf)
       (retract ?task)
       (assert (task ask-user))
    )

    ;----------------------------------------------------------------------------
    ; acceptance ends the session on the correct obsequious note.

    ;; ACCEPTANCE
    (defrule acceptance
        ?task<-(task choice)
        (decision (re ?candidate) (is yes))
        => 
        (printout t crlf "Sir/Madam has impeccable taste" t crlf)
        (retract ?task)
        (assert (task ask-user))
    )

    ;; RESET-PROGRAM
    ;----------------------------------------------------------------------------
    ;; y - restart program
    ;; n - terminate program
    ;----------------------------------------------------------------------------

    (defrule reset-program
       ?task<-(task ask-user)
       =>
       (printout t crlf "Would you like to start over? (y/n): " )
       (bind ?ans(read))
       (if (eq (str-compare ?ans y) 0)
           then (reset)
                (run)
       else
           (retract ?task))
    )

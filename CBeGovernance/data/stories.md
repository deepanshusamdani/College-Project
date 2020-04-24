## howbuilt
* ask_howbuilt
    - utter_ask_howbuilt

## howold
* ask_howold
    - utter_ask_howold

## isbot
* ask_isbot
    - utter_ask_isbot

## languagesbot
* ask_languagesbot
    - utter_ask_languagesbot

## restaurant
* ask_restaurant
    - utter_ask_restaurant
	
## time
* ask_time
    - utter_ask_time

## whatismyname
* ask_whatismyname
    - utter_ask_whatismyname

## wherefrom
* ask_wherefrom
    - utter_ask_wherefrom

## whoami
* ask_whoami
    - utter_ask_whoami

## builder
* ask_builder
    - utter_ask_builder

## howdoing
* ask_howdoing
    - utter_ask_howdoing

## weather
* ask_weather
    - utter_ask_weather

## whatspossible
* ask_whatspossible
    - utter_ask_whatspossible

## whoisit
* ask_whoisit
    - utter_ask_whoisit

## bye
* bye
    - utter_bye

## canthelp
* canthelp
    - utter_canthelp

## greet
* greet
    - utter_greet

## human_handoff
* human_handoff
    - utter_human_handoff

## out_of_scope
* out_of_scope
    - utter_out_of_scope

## thank
* thank
    - utter_thank
	- utter_anything_else

## ask_areyouupdated
* ask_areyouupdated
    - utter_ask_areyouupdated

## laugh
* laugh
    - utter_laugh

## specify
* ask_scheme OR ask_scheme{"infotype": "schemes"}
    - utter_specify
	- utter_ask_whatspossible

## about source
* ask_scheme{"source": "rbi"}
	- action_source
    - slot{"source": "rbi"}
	- utter_knowmore

## scheme
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}

## specific scheme
* ask_specific_scheme{"scheme_name": "National Livestock Mission"}
    - action_specific_scheme
    - slot{"scheme_name": "National Livestock Mission"}

## story 01
* greet
    - utter_greet
* ask_isbot
    - utter_ask_isbot
* ask_howbuilt
    - utter_ask_howbuilt
* ask_howold
    - utter_ask_howold
* ask_languagesbot
    - utter_ask_languagesbot

## story 02
* greet
    - utter_greet
* ask_isbot
    - utter_ask_isbot
* ask_builder
    - utter_ask_builder
* ask_howbuilt
    - utter_ask_howbuilt
* ask_howold
    - utter_ask_howold
* ask_languagesbot
    - utter_ask_languagesbot
	
## story 03
* greet
    - utter_greet
* ask_isbot
    - utter_ask_isbot
* ask_howold
    - utter_ask_howold
* ask_howbuilt
    - utter_ask_howbuilt
* ask_builder
    - utter_ask_builder
* ask_languagesbot
    - utter_ask_languagesbot

## story 04
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "nabard", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "nabard", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Dairy Entrepreneurship Development Scheme"}
    - action_specific_scheme
    - slot{"scheme_name": "Dairy Entrepreneurship Development Scheme"}
* thank
	- utter_anything_else
* deny
    - utter_thankyou
* bye
    - utter_bye
	
## story 05
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "dfs", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "dfs", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Pradhan Mantri Jan Dhan Yojana"}
    - action_specific_scheme
    - slot{"scheme_name": "Pradhan Mantri Jan Dhan Yojana"}
* thank
	- utter_anything_else
* affirm
    - utter_what_help

## story 06
* greet
    - utter_greet
* ask_howdoing
    - utter_ask_howdoing
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
    - action_specific_scheme
    - slot{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
* thank
	- utter_anything_else
* deny
    - utter_thankyou
* bye
    - utter_bye

## story 07
* greet
    - utter_greet
* ask_howdoing
    - utter_ask_howdoing
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Lead Bank Scheme"}
    - action_specific_scheme
    - slot{"scheme_name": "Lead Bank Scheme"}
* thank
	- utter_anything_else
* affirm
    - utter_what_help

## story 08
* greet
    - utter_greet
* ask_howdoing
    - utter_ask_howdoing
* ask_scheme OR ask_scheme{"infotype": "schemes"}
    - utter_specify
	- utter_ask_whatspossible
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Kisan Credit Card Scheme"}
    - action_specific_scheme
    - slot{"scheme_name": "Kisan Credit Card Scheme"}
* thank
	- utter_anything_else
* deny
    - utter_thankyou
* bye
    - utter_bye

## story 09
* greet
    - utter_greet
* ask_howdoing
    - utter_ask_howdoing
* ask_scheme OR ask_scheme{"infotype": "schemes"}
    - utter_specify
	- utter_ask_whatspossible
* ask_scheme{"source": "dfs", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "dfs", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "From Jan Dhan to Jan Suraksha"}
    - action_specific_scheme
    - slot{"scheme_name": "From Jan Dhan to Jan Suraksha"}
* thank
	- utter_anything_else
* affirm
    - utter_what_help

## story 10
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* canthelp
    - utter_canthelp
* bye
    - utter_bye

## story 11
* greet
    - utter_greet
* ask_scheme OR ask_scheme{"infotype": "schemes"}
    - utter_specify
	- utter_ask_whatspossible
* ask_scheme{"source": "nabard", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "nabard", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Credit Linked Capital Subsidy Scheme"}
    - action_specific_scheme
    - slot{"scheme_name": "Credit Linked Capital Subsidy Scheme"}
* canthelp
    - utter_canthelp
* bye
    - utter_bye

## story 12
* greet
    - utter_greet
* ask_scheme OR ask_scheme{"infotype": "schemes"}
    - utter_specify
	- utter_ask_whatspossible
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Lead Bank Scheme"}
    - action_specific_scheme
    - slot{"scheme_name": "Lead Bank Scheme"}
* canthelp
    - utter_canthelp
* human_handoff
    - utter_human_handoff

## story 13
* greet
    - utter_greet
* ask_scheme OR ask_scheme{"infotype": "schemes"}
    - utter_specify
	- utter_ask_whatspossible
* ask_scheme{"source": "dfs", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "dfs", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Pradhan Mantri Jeevan Jyoti Bima Yojana"}
    - action_specific_scheme
    - slot{"scheme_name": "Pradhan Mantri Jeevan Jyoti Bima Yojana"}
* ask_areyouupdated
    - utter_ask_areyouupdated
* canthelp
    - utter_canthelp
* human_handoff
    - utter_human_handoff

## story 14
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "nabard", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "nabard", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Interest Subvention Scheme"}
    - action_specific_scheme
    - slot{"scheme_name": "Interest Subvention Scheme"}
* thank
	- utter_anything_else
* deny
    - utter_thankyou
* bye
    - utter_bye

## story 15
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
    - action_specific_scheme
    - slot{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
* thank
	- utter_anything_else
* affirm
    - utter_what_help

## story 16
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}
* ask_specific_scheme{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
    - action_specific_scheme
    - slot{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
* thank
    - utter_thank
* bye
    - utter_bye

## story 17
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_specific_scheme{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
    - action_specific_scheme
    - slot{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
* thank
	- utter_anything_else
* affirm
    - utter_what_help

## story 18
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_specific_scheme{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
    - action_specific_scheme
    - slot{"scheme_name": "Deendayal Antyodaya Yojana in NULM"}
* thank
    - utter_thank
* bye
    - utter_bye

## story 19
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}
* thank
	- utter_anything_else
* affirm
    - utter_what_help

## story 20
* greet
    - utter_greet
* ask_whatspossible
    - utter_ask_whatspossible
* ask_scheme{"source": "rbi", "infotype": "schemes"}
    - action_scheme
    - slot{"source": "rbi", "infotype": "schemes"}
* thank
    - utter_thank
* bye
    - utter_bye
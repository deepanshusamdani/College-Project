from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

from dbconnect import connection
import gc

class ActionScheme(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return 'action_scheme'
	
    def run(self, dispatcher, tracker, domain):
        curs, conn = connection()
        source = tracker.get_slot('source')
        query = "select scheme_name from schemes where scheme_source='%s'" % (source, )
        curs.execute(query)
        results = curs.fetchall()
        for r in results:
            dispatcher.utter_message("Scheme Name: "+r[0]+"\n")  # send the message back to the user
        curs.close()
        conn.close()
        gc.collect()
        dispatcher.utter_message("If you want to know more details about a particular scheme from above list, ask me something like, 'tell me about scheme_name_from_above'. Remember name of scheme must be exact.")
        if source=='rbi':
            dispatcher.utter_message("For further information, you may visit: https://www.rbi.org.in/Scripts/NotificationUser.aspx")
        elif source=='nabard':
            dispatcher.utter_message("For further information, you may visit: https://www.nabard.org/content1.aspx?id=23&catid=23&mid=530")
        elif source=='dfs':
            dispatcher.utter_message("For further information, you may visit: https://financialservices.gov.in/new-initiatives/schemes")
        return [SlotSet('source',source)]	#syntax: SlotSet('slot_name', var_name)
		
class ActionSource(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return 'action_source'
	
    def run(self, dispatcher, tracker, domain):
        source = tracker.get_slot('source')
        if source=='rbi':
            dispatcher.utter_message("The Reserve Bank of India (RBI) is India's central banking institution, which controls the issuance and supply of the Indian rupee.")
        elif source=='nabard':
            dispatcher.utter_message("National Bank for Agriculture and Rural Development (NABARD) is an apex development financial institution in India, that has been entrusted with matters concerning policy, planning and operations in the field of credit for agriculture and other economic activities in rural areas in India.")
        elif source=='dfs':
            dispatcher.utter_message("The Department of Financial Services (DFS) oversees several key programs/initiatives and reforms of the Government concerning the Banking Sector, the Insurance Sector and the Pension Sector in India.")
        return [SlotSet('source',source)]	#syntax: SlotSet('slot_name', var_name)
		
class ActionSpecificScheme(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return 'action_specific_scheme'
	
    def run(self, dispatcher, tracker, domain):
        curs, conn = connection()
        scheme_name = tracker.get_slot('scheme_name')
        query = "select scheme_name, scheme_detail, scheme_link from schemes where scheme_name='%s'" % (scheme_name, )
        curs.execute(query)
        results = curs.fetchall()
        for r in results:
            dispatcher.utter_message("Scheme Name: "+r[0]+"\nScheme Details: "+r[1])  # send the message back to the user
            dispatcher.utter_message("For more information of this scheme, please visit: "+r[2])
        curs.close()
        conn.close()
        gc.collect()
        return [SlotSet('scheme_name',scheme_name)]	#syntax: SlotSet('slot_name', var_name)
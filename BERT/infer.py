# import sys
# sys.path.insert(0, './sat_final')
# sys.path.insert(0, './BERT')

from bert import QA


if __name__ == '__main__':


    model = QA('model')

    doc = "Victoria has a written constitution enacted in 1975, but based on the 1855 colonial constitution, passed by the United Kingdom Parliament as the Victoria Constitution Act 1855, which establishes the Parliament as the state's law-making body for matters coming under state responsibility. The Victorian Constitution can be amended by the Parliament of Victoria, except for certain 'entrenched' provisions that require either an absolute majority in both houses, a three-fifths majority in both houses, or the approval of the Victorian people in a referendum, depending on the provision."

    q = 'When did Victoria enact its constitution?'

    answer = model.predict(doc,q)

    print(answer['answer'])
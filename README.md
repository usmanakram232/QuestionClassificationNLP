Question Classification
=======================
Course: Natural Language Processing and Information Retrieval <br/>
Instructor: [_Alessandro Moschitti_](http://disi.unitn.it/moschitti/teaching.html)

**Objective**: Using Tree Kernels for question classification.

Tasks:
 - Separate labels and questions
 - Parse (English grammer using Stanford Parser), create trees 
 - Features
 - Train Tree kernel
 - Test on TREC 2010
<br/>![Example Tree from a question](/okay_step_1.PNG "Example Tree from a question")<br/>Example Tree from a question

Data: TREC 2012 for testing and training questions from "[Experimental Data for Question Classification](http://cogcomp.cs.illinois.edu/Data/QA/QC/)."

Folders:
- data
  - .label (label Question)
  - .lbl (only label)
  - .q (only questions)
  - .portStem (questions after using Porter stemmer)
  - .stemmed (questions after using Paice/Husk stemmer)
  
  
#####**Definition of Question Classes**

| **Class**         | **Definition**    |
|:------------------|:------------------|
|**ABBREVIATION**   | abbreviation      |
|  abb	            | abbreviation      |
|  exp	            | expression abbreviated      |
|**ENTITY**	        | entities      |
|  animal	        | animals      |
|  body	            | organs of body      |
|  color	        | colors      |
|  creative	        | inventions, books and other creative pieces      |
|  currency	        | currency names      |
|  dis.med.	        | diseases and medicine      |
|  event	        | events      |
|  food	            | food      |
|  instrument	    | musical instrument      |
|  lang	            | languages      |
|  letter	        | letters like a-z      |
|  other	        | other entities      |
|  plant	        | plants      |
|  product	        | products      |
|  religion	        | religions      |
|  sport	        | sports      |
|  substance	    | elements and substances      |
|  symbol	        | symbols and signs      |
|  technique	    | techniques and methods      |
|  term	            | equivalent terms      |
|  vehicle	        | vehicles      |
|  word	            | words with a special property      |
|**DESCRIPTION**	| description and abstract concepts      |
|  definition	    | definition of sth.      |
|  description	    | description of sth.      |
|  manner	        | manner of an action      |
|  reason	        | reasons      |
|**HUMAN**	        | human beings      |
|  group	        | a group or organization of persons      |
|  ind	            | an individual      |
|  title	        | title of a person      |
|  description	    | description of a person      |
|**LOCATION**	    | locations      |
|  city	            | cities      |
|  country	        | countries      |
|  mountain	        | mountains      |
|  other	        | other locations      |
|  state	        |states      |
|**NUMERIC**	|numeric values      |
|  code	    |postcodes or other codes      |
|  count	|number of sth.      |
|  date	    |dates      |
|  distance	|linear measures      |
|  money	|prices      |
|  order	|ranks      |
|  other	|other numbers      |
|  period	|the lasting time of sth.      |
|  percent	|fractions      |
|  speed	|speed      |
|  temp	    |temperature      |
|  size	    |size, area and volume      |
|  weight	| weight      |
  
Languages and tools used
- [*Python*](http://sourceforge.net/projects/winpython/) - WinPython
 - [nltk](http://www.nltk.org)
 - [nlpnet](http://nilc.icmc.usp.br/nlpnet/)
- **Java**
 - [Stanford Tokenizer](http://nlp.stanford.edu/software/lex-parser.shtml)
 - [Stanford NER](http://nlp.stanford.edu/software/CRF-NER.shtml)
 - [The GATE Predicate-Argument EXtractor Component](www.semanticsoftware.info/pax)
 - Stemmers [optional]
   - [Paice/Husk Stemmer](http://www.comp.lancs.ac.uk/computing/research/stemming/Links/implementations.htm)
    - [Porter Stemmer](http://www.tartarus.org/~martin/PorterStemmer)
- [SENNA: A Fast Semantic Role Labeling](ml.nec-labs.com/senna/)
- [Toolkit for Advanced Discriminative Modeling](http://tadm.sourceforge.net/)
- [Malt Parser](www.maltparser.org/download.html)
- [Hunpos Tagger](https://code.google.com/p/hunpos/downloads/list)
- batch scripting


###### References
 [Installing Third Party Software on NLTK](https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software)
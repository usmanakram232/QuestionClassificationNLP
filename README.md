Question Classification
=======================
Course: Natural Language Processing and Information Retrieval </br>
Instructor: [_Alessandro Moschitti_](http://disi.unitn.it/moschitti/teaching.html)

Task: Using Tree Kernels for question classification.

Data: TREC 2012 for testing and training questions from "[Experimental Data for Question Classification](http://cogcomp.cs.illinois.edu/Data/QA/QC/)."

Stemmers used:
- [Porter stemmer](http://www.tartarus.org/~martin/PorterStemmer)
- [Paice/Husk Stemmer](http://www.comp.lancs.ac.uk/computing/research/stemming/Links/implementations.htm)

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
  
Languages used *Java*, *Python*, and bat scripting.

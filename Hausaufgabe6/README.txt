# Grammatik einlesen
grammar = read_file("grammatik.txt")
# Regeln parsen
rules = read_grammar(grammar)
# NP-Regeln extrahieren (beispielhafte Anfrage
# -- andere Kategorien sollten natuerlich ebenfalls moeglich sein)
subset = extract_rules("NP",rules)
# Subset ausgeben
write_grammar(outfile,subset)
# Baumbank einlesen
treebank = read_file("tueba5000.penn")
# Baeume parsen
rules = read_treebank(treebank)
# Grammatik ausgeben
write_grammar_in_file("grammatik.txt",rules)


# NX-Regeln
NX --> NN
NX --> ART NN

( VROOT
( SIMPX

( LK
( VXFIN
( VVFIN Veruntreute )
)
)

( MF
( NX=ORG
( ART die )
 ( NN AWO )
 )
 ( NX
 ( NN Spendengeld )
 ) )
  )
  ( $. ? )
   )



( VROOT ( NX ( NX ( NN Landesvorsitzende ) ) ( NX=PER ( NE Ute ) ( NE Wedemeier ) ) ) ( $. : ) ( NX ( ART Ein ) ( NN Buchungsfehler ) ) )
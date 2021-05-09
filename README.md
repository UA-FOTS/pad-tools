# PAD Tools
Library to manipulate Presburger arithmetic formulas with divisibility

![Tests badge](https://github.com/UA-FOTS/pad-tools/actions/workflows/main.yml/badge.svg)

## Functionality
- [X] Parse prenex normal form PAD formulas
- [X] Output quantifier-free expression part of a formula as dot string/file
- [X] Evaluate an expression on a given variable valuation
- [X] Negation normal form, disjunctive normal form transformations
- [X] Lechner normal form (DNF with no negations on predicates) transformation
- [ ] ...

## Notes
- The formula parser was generated using antlr4 and the grammar used is also
  included (see PAD.g4).
- The parser accepts PAD formulas in prenex normal form.

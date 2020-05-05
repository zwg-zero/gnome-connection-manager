PCRE2_FLAGS=1074398208 #PCRE2_UTF | PCRE2_NO_UTF_CHECK | PCRE2_UCP | PCRE2_MULTILINE
DIRECT="(?<APOS_START>(?<='))?(?(DEFINE)(?<S4>(?x: (?: [0-9] | [1-9][0-9] | 1[0-9]{2} | 2[0-4][0-9] | 25[0-5] ) (?! [0-9] ) )))(?(DEFINE)(?<IPV4>(?x: (?: (?&S4) \. ){3} (?&S4) )))(?(DEFINE)(?<S6>[[:xdigit:]]{1,4})(?<CS6>:(?&S6))(?<S6C>(?&S6):))(?(DEFINE)(?<IPV6>(?x: (?: (?x: :: ) | (?x: : (?&CS6){1,7} ) | (?x: (?! (?: [[:xdigit:]]*: ){8} ) (?&S6C){1,6} (?&CS6){1,6} ) | (?x: (?&S6C){1,7} : ) | (?x: (?&S6C){7} (?&S6) ) | (?: (?x: (?&S6C){6} ) | (?x: :: (?&S6C){0,5} ) | (?x: (?! (?: [[:xdigit:]]*: ){7} ) (?&S6C){1,4} (?&CS6){1,4} ) : | (?x: (?&S6C){1,5} : ) ) (?&IPV4) ) (?! [.:[:xdigit:]] ) )))(?(DEFINE)(?<PATH_INNER>(?x: (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?: \( (?&PATH_INNER) \) | \[ (?&PATH_INNER) \] ) )* [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* )))(?(DEFINE)(?<PATH>(?x: (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?: \( (?&PATH_INNER) \) | \[ (?&PATH_INNER) \] ) )* (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?(<APOS_START>)[-[:alnum:]\Q_$+*:@&=/~#|%\E]|[-[:alnum:]\Q_$+*:@&=/~#|%'\E]) )? )))(?ix: news | telnet | nntp | https? | ftps? | sftp | webcal )://(?:[-+.[:alnum:]]+(?x: :[-[:alnum:]\Q,?;.:/!%$^*&~"#'\E]* )?@)?(?x: (?x: (?: (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )+ \. )* (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )* (?! [0-9] ) (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )+ ) | (?&IPV4) | \[ (?&IPV6) \] )(?x: \:(?x: (?: [1-9][0-9]{0,3} | [1-5][0-9]{4} | 6[0-4][0-9]{3} | 65[0-4][0-9]{2} | 655[0-2][0-9] | 6553[0-5] ) (?! [0-9] ) ) )?(?x: /(?&PATH) )?"
URL="(?<APOS_START>(?<='))?(?<!(?:(?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )|[.]))(?=(?i:www|ftp))(?x: (?: (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )+ \. )* (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )* (?! [0-9] ) (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )+ )(?x: \:(?x: (?: [1-9][0-9]{0,3} | [1-5][0-9]{4} | 6[0-4][0-9]{3} | 65[0-4][0-9]{2} | 655[0-2][0-9] | 6553[0-5] ) (?! [0-9] ) ) )?(?(DEFINE)(?<PATH_INNER>(?x: (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?: \( (?&PATH_INNER) \) | \[ (?&PATH_INNER) \] ) )* [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* )))(?(DEFINE)(?<PATH>(?x: (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?: \( (?&PATH_INNER) \) | \[ (?&PATH_INNER) \] ) )* (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?(<APOS_START>)[-[:alnum:]\Q_$+*:@&=/~#|%\E]|[-[:alnum:]\Q_$+*:@&=/~#|%'\E]) )? )))(?x: /(?&PATH) )?"
EMAIL="(?<APOS_START>(?<='))?(?(DEFINE)(?<S4>(?x: (?: [0-9] | [1-9][0-9] | 1[0-9]{2} | 2[0-4][0-9] | 25[0-5] ) (?! [0-9] ) )))(?(DEFINE)(?<IPV4>(?x: (?: (?&S4) \. ){3} (?&S4) )))(?(DEFINE)(?<S6>[[:xdigit:]]{1,4})(?<CS6>:(?&S6))(?<S6C>(?&S6):))(?(DEFINE)(?<IPV6>(?x: (?: (?x: :: ) | (?x: : (?&CS6){1,7} ) | (?x: (?! (?: [[:xdigit:]]*: ){8} ) (?&S6C){1,6} (?&CS6){1,6} ) | (?x: (?&S6C){1,7} : ) | (?x: (?&S6C){7} (?&S6) ) | (?: (?x: (?&S6C){6} ) | (?x: :: (?&S6C){0,5} ) | (?x: (?! (?: [[:xdigit:]]*: ){7} ) (?&S6C){1,4} (?&CS6){1,4} ) : | (?x: (?&S6C){1,5} : ) ) (?&IPV4) ) (?! [.:[:xdigit:]] ) )))(?(DEFINE)(?<PATH_INNER>(?x: (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?: \( (?&PATH_INNER) \) | \[ (?&PATH_INNER) \] ) )* [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* )))(?(DEFINE)(?<PATH>(?x: (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?: \( (?&PATH_INNER) \) | \[ (?&PATH_INNER) \] ) )* (?: [-[:alnum:]\Q_$.+!*,:;@&=?/~#|%'\E]* (?(<APOS_START>)[-[:alnum:]\Q_$+*:@&=/~#|%\E]|[-[:alnum:]\Q_$+*:@&=/~#|%'\E]) )? )))(?i:mailto:)?[-+.[:alnum:]]+@(?x: (?x: (?: (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )+ \.)+ (?x: (?: (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )+ \. )* (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )* (?! [0-9] ) (?x: [-[:alnum:]] | (?! [[:ascii:]] ) [[:graph:]] )+ ) ) | \[ (?: (?&IPV4) | (?&IPV6) ) \] )"

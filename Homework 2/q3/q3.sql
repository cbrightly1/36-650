
                               Table "public.rdata"
 Column |     Type     | Collation | Nullable |              Default
--------+--------------+-----------+----------+-----------------------------------
 id     | integer      |           | not null | nextval('rdata_id_seq'::regclass)
 a      | text         |           | not null |
 b      | text         |           | not null |
 moment | date         |           |          | '2020-01-01'::date
 x      | numeric(5,2) |           |          |
Indexes:
    "rdata_pkey" PRIMARY KEY, btree (id)
    "rdata_a_key" UNIQUE CONSTRAINT, btree (a)
    "rdata_b_key" UNIQUE CONSTRAINT, btree (b)
Check constraints:
    "rdata_a_check" CHECK (char_length(a) > 0)
    "rdata_a_check1" CHECK (char_length(a) > 0)
    "rdata_x_check" CHECK (x > 0::numeric)


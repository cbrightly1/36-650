ALTER TABLE player_bios 
ADD COLUMN position TEXT;

UPDATE player_bios
SET position = (SELECT n.position FROM new_table n
where n.player = player_bios.id);

SELECT firstname, lastname, position from player_bios
limit 5;

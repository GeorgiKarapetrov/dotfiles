#modern sql
#https://www.youtube.com/watch?v=w5J_WrcjwR0
#PostGreSQL game example

begin
raise notice 'po'
do $game$ begin
    set search_path = game, state, public
    insert into civ (name) vlues ('ear');
    insert into civ (name) vlues ('ear');
end $game$
insert into dev_jing_dw.ads_user_session_269_test
SELECT
wid as mid,
openid,
current_date as calculated_at,
create_time,
session_id,
type,
session_position,
session_depth,
last_create_time - first_value(create_time) over openid_sess_with_pos_asc as session_duration,
30 as session_event_max_duration,
session_event_duration
FROM
(
SELECT
openid,
wid,
create_time,
session_id,
type,
session_position,
first_value(session_position) over openid_sess_with_pos_desc as session_depth,
first_value(create_time) over openid_sess_with_pos_desc as last_create_time,
lag(create_time) over openid_sess_with_pos_desc - create_time as session_event_duration
FROM(
SELECT
openid,
wid,
create_time,
session_id,
type,
row_number() over openid_sess as session_position
FROM
(
SELECT openid,
       wid,
       create_time,
       concat_ws('_', 'sess', openid, cast(((SUM(case new_session when true then 1 when false then 0 end) OVER sess) + 1) as varchar)) as session_id,
        type
FROM
  ( SELECT openid,
         wid,
           type,
           create_time,
         case
          LAG(create_time) OVER ua is null
           when
          true
        then
          false
        when
          false
        then
          create_time - LAG(create_time) OVER ua > 1800
        end AS new_session
   FROM dev_jing_dw.jing_user_action_record
   WINDOW ua AS  (PARTITION BY openid ORDER BY create_time ASC)
  ) AS t_ua
  WINDOW sess AS  (PARTITION BY openid ORDER BY create_time ASC)
  ) AS t_sess
  WINDOW openid_sess AS  (PARTITION BY session_id ORDER BY create_time ASC)
  ) AS t_sess_with_pos
  WINDOW openid_sess_with_pos_desc AS  (PARTITION BY session_id ORDER BY create_time DESC)
  ) AS t_sess_with_depth
  WINDOW openid_sess_with_pos_asc AS  (PARTITION BY session_id ORDER BY create_time ASC)
;

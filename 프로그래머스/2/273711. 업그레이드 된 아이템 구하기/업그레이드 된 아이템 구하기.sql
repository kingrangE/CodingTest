
SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I
JOIN ITEM_TREE T # 아이템 별 부모 아이템 번호를 찾기
    ON I.ITEM_ID = T.ITEM_ID
JOIN ITEM_INFO I2 # 그 부모 아이템 번호가 어떤 아이템인지 알기 위해
    ON I2.ITEM_ID = T.PARENT_ITEM_ID 
# 여기까지 하면, 아이템 별, 부모 아이템이 뭔지 알 수 있음 (NULL 제외)
WHERE I2.RARITY = 'RARE' # 기존 아이템이 RARE인거

ORDER BY I.ITEM_ID DESC # 내림차순 정렬



Projects.objects.all().filter(parent_id=166, )

hero_qs = Hero.objects.filter(
    category=OuterRef("pk")
).order_by("-projeto_factor")
Category.objects.all().annotate(
    most_benevolent_hero=Subquery(
        hero_qs.values('name')[:1]
    )
)



# SELECT "entities_category"."id",
#        "entities_category"."name",

#   (SELECT U0."name"
#    FROM "entities_hero" U0
#    WHERE U0."category_id" = ("entities_category"."id")
#    ORDER BY U0."benevolence_factor" DESC
#    LIMIT 1) AS "most_benevolent_hero"
# FROM "entities_category
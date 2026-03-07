# Generated manually - 新增 Product 範例資料

from django.db import migrations


def create_products(apps, schema_editor):
    Product = apps.get_model("ecommerce", "Product")
    products_data = [
        {"name": "經典白襯衫", "price": "890.00", "description": "100% 棉質，舒適透氣，百搭必備。"},
        {"name": "休閒牛仔褲", "price": "1290.00", "description": "修身剪裁，彈性布料，耐穿好搭。"},
        {"name": "針織開襟外套", "price": "1580.00", "description": "柔軟針織，春秋必備單品。"},
        {"name": "帆布托特包", "price": "590.00", "description": "大容量、耐磨，日常外出首選。"},
        {"name": "皮革皮帶", "price": "450.00", "description": "真皮材質，簡約扣頭設計。"},
        {"name": "運動跑鞋", "price": "2280.00", "description": "輕量透氣，適合慢跑與日常穿著。"},
        {"name": "毛呢寬簷帽", "price": "680.00", "description": "秋冬防風保暖，造型加分。"},
        {"name": "不鏽鋼保溫瓶", "price": "750.00", "description": "500ml，保冷保溫，環保隨身。"},
    ]
    for data in products_data:
        Product.objects.get_or_create(
            name=data["name"],
            defaults={"price": data["price"], "description": data["description"]},
        )


def remove_products(apps, schema_editor):
    Product = apps.get_model("ecommerce", "Product")
    names = [
        "經典白襯衫", "休閒牛仔褲", "針織開襟外套", "帆布托特包",
        "皮革皮帶", "運動跑鞋", "毛呢寬簷帽", "不鏽鋼保溫瓶",
    ]
    Product.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_products, remove_products),
    ]

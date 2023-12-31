# Generated by Django 4.2.6 on 2023-10-16 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('short_description', models.TextField()),
                ('sku', models.CharField(max_length=50, verbose_name='SKU')),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('sale_price', models.FloatField()),
                ('description', models.TextField()),
                ('banner_icon', models.ImageField(blank=True, null=True, upload_to='product_banners/')),
                ('icon_section_text', models.TextField(blank=True, null=True)),
                ('review_next_section_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('review_next_section_subheading', models.CharField(blank=True, max_length=255, null=True)),
                ('review_next_section_description', models.TextField(blank=True, null=True)),
                ('benefits_heading_number', models.CharField(blank=True, max_length=255, null=True)),
                ('benefits_heading_text', models.CharField(blank=True, max_length=255, null=True)),
                ('benefits_description', models.TextField(blank=True, null=True)),
                ('benefits_bottom_text', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_users_field', related_query_name='category_users_field', to='categories.categorymodel')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductReviewsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_Review_users_field', related_query_name='Product_Review_users_field', to='products.productmodel')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_Review_users_field', related_query_name='Product_Review_users_field', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product_Review',
                'verbose_name_plural': 'Product_Reviews',
                'db_table': 'Product_Review',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product_discussionsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='product_discussion_icons/')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product_discussion_users_field', related_query_name='Product_discussion_users_field', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'Product_discussion',
                'verbose_name_plural': 'Product_discussions',
                'db_table': 'Product_discussion',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='IngredientsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='ingredients/')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Ingredient_users_field', related_query_name='Ingredient_users_field', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
                'db_table': 'Ingredient',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='IconSectionsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon_section_2_icons/')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='IconSection_users_field', related_query_name='IconSection_users_field', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'IconSection',
                'verbose_name_plural': 'IconSections',
                'db_table': 'IconSection',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(upload_to='product_gallery/')),
                ('is_featured', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Gallery_users_field', related_query_name='Gallery_users_field', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
                'db_table': 'Gallery',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Faq_next_section_iconsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='faq_next_section_icons/')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Faq_next_section_icon_users_field', related_query_name='Faq_next_section_icon_users_field', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'Faq_next_section_icon',
                'verbose_name_plural': 'Faq_next_section_icons',
                'db_table': 'Faq_next_section_icon',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BenefitsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Benefit_users_field', related_query_name='Benefit_users_field', to='products.productmodel')),
            ],
            options={
                'verbose_name': 'Benefit',
                'verbose_name_plural': 'Benefits',
                'db_table': 'Benefit',
                'ordering': ['-created_at'],
            },
        ),
    ]

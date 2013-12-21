# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('bookstore_proper_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('bookstore_proper', ['Author'])

        # Adding model 'Publisher'
        db.create_table('bookstore_proper_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('bookstore_proper', ['Publisher'])

        # Adding model 'Book'
        db.create_table('bookstore_proper_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bookstore_proper.Publisher'], null=True)),
            ('publication_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=13, null=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
        ))
        db.send_create_signal('bookstore_proper', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name('bookstore_proper_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['bookstore_proper.book'], null=False)),
            ('author', models.ForeignKey(orm['bookstore_proper.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('bookstore_proper_author')

        # Deleting model 'Publisher'
        db.delete_table('bookstore_proper_publisher')

        # Deleting model 'Book'
        db.delete_table('bookstore_proper_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name('bookstore_proper_book_authors'))


    models = {
        'bookstore_proper.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'bookstore_proper.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bookstore_proper.Author']", 'symmetrical': 'False', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bookstore_proper.Publisher']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'bookstore_proper.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['bookstore_proper']
import anki
from anki.exporting import AnkiPackageExporter
import os

TMPDIR = "/tmp"
FBASENAME = "test"
FONAME = "/home/rainman/testdata/test.apkg"

collection = anki.Collection(os.path.join(TMPDIR, 'collection.anki2'))

deck_id = collection.decks.id(FBASENAME + "_deck")
deck = collection.decks.get(deck_id)

deck['mid'] = collection.models.byName('Cloze')

model = collection.models.new(FBASENAME + "_model")
model['tags'].append(FBASENAME + "_tag")
model['did'] = deck_id
model['css'] = """
.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
.from {
  font-style: italic;
}
"""

collection.models.addField(model, collection.models.newField('en'))
collection.models.addField(model, collection.models.newField('ru'))

tmpl = collection.models.newTemplate('en -> ru')
tmpl['qfmt'] = '<div class="from">{{en}}</div>'
tmpl['afmt'] = '{{FrontSide}}\n\n<hr id=answer>\n\n{{ru}}'
collection.models.addTemplate(model, tmpl)
tmpl = collection.models.newTemplate('ru -> en')
tmpl['qfmt'] = '{{ru}}'
tmpl['afmt'] = '{{FrontSide}}\n\n<hr id=answer>\n\n<div class="from">{{en}}</div>'
collection.models.addTemplate(model, tmpl)

model['id'] = 12345678  # essential for upgrade detection
collection.models.update(model)
collection.models.setCurrent(model)
collection.models.save(model)

note = anki.notes.Note(collection, model)
note['en'] = "hello"
note['ru'] = u"[heləʊ]\nint. привет"
note.guid = "xxx1"
collection.addNote(note)

note = collection.newNote()
note['en'] = "bye"
note['ru'] = u"[baɪ]\nint. пока"
note.guid = "xxx2"
collection.addNote(note)

export = AnkiPackageExporter(collection)
export.exportInto(FONAME)

# coding: utf-8
from biblat_schema.models import SubDisciplina, Disciplina
from biblat_schema.catalogs import I18NField, Idioma
from .base import BaseTestCase


class TestSubdisciplineModel(BaseTestCase):
    model_class_to_delete = [SubDisciplina, Disciplina, I18NField, Idioma]

    def _crea_idioma(self):
        _id = self.generate_uuid_32_string()
        nombre = {
            'es': 'Español',
            'en': 'Spanish'
        }
        idioma_data = {
            '_id': _id,
            'iso_639_1': 'es',
            'iso_639_2': 'spa',
            'nombre': nombre
        }
        return Idioma(**idioma_data)

    def _crea_disciplina(self):
        _id = self.generate_uuid_32_string()
        nombre = self._crea_nombre()
        disciplina_data = {
            '_id': _id,
            'nombre': nombre
        }
        return Disciplina(** disciplina_data)

    def _crea_nombre(self):
        sub_disciplina_data = {
            'es': 'Biologia',
            'en': 'Biology'
        }
        return I18NField(** sub_disciplina_data)

    def test_solo_campos_requeridos(self):
        # Datos
        _id = self.generate_uuid_32_string()
        disciplina = self._crea_disciplina()
        nombre = I18NField(**{
            'es': 'Biologia',
            'en': 'Biology'
        })
        subdisciplina_data = {
            '_id': _id,
            'disciplina': disciplina,
            'nombre': nombre
        }

        # Guardamos
        subdisciplina_doc = SubDisciplina(**subdisciplina_data)

        # Comprobamos
        self.assertEqual(subdisciplina_data['_id'],
                         subdisciplina_doc.id)
        self.assertEqual(subdisciplina_data['disciplina'],
                         subdisciplina_doc.disciplina)
        self.assertEqual(subdisciplina_data['nombre'],
                         subdisciplina_doc.nombre)

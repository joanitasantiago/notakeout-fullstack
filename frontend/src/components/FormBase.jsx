import Button from './Button';
import './FormBase.css';

function FormBase({
  title,
  fields,
  values,
  onChange,
  onSubmit,
  onCancel,
  submitLabel = 'Salvar',
  cancelLabel = 'Cancelar',
}) {
  return (
    <form onSubmit={onSubmit} className="form-box">
      <h3>{title}</h3>

      {fields.map((field) => (
        <div className="form-input-group" key={field.name}>
          {field.type === 'checkbox' ? (
            <label>
              <input
                type="checkbox"
                name={field.name}
                checked={values[field.name] || false}
                onChange={onChange}
              />
              {field.label}
            </label>
          ) : (
            <>
              <label htmlFor={field.name}>{field.label}</label>
              <input
                type={field.type || 'text'}
                id={field.name}
                name={field.name}
                value={values[field.name] || ''}
                onChange={onChange}
                required={field.required}
                placeholder={field.placeholder}
              />
            </>
          )}
        </div>
      ))}
      <Button type="submit">{submitLabel}</Button>
      <Button type="button" variant="danger" onClick={onCancel}>
        {cancelLabel}
      </Button>
    </form>
  );
}

export default FormBase;

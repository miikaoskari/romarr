import React, { Fragment, useState } from 'react';
import { Switch, Dialog, Transition } from '@headlessui/react';
import { Button } from '../index';
import propTypes from 'prop-types';
import TextField from '../textfield/TextField';

const Modal = ({ isOpen, closeModal, title }) => {
  const [enabled, setEnabled] = useState(false);
  return (
    <Transition appear show={isOpen} as={Fragment}>
      <Dialog as="div" className="relative z-10" onClose={closeModal}>
        <Transition.Child
          as={Fragment}
          enter="ease-out duration-300"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in duration-200"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-black/25" />
        </Transition.Child>

        <div className="fixed inset-0 overflow-y-auto">
          <div className="flex min-h-full items-center justify-center p-4 text-center">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0 scale-95"
              enterTo="opacity-100 scale-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100 scale-100"
              leaveTo="opacity-0 scale-95"
            >
              <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                <Dialog.Title as="h3" className="text-lg font-medium leading-6 text-gray-900">
                  {title}
                </Dialog.Title>
                <div className="mt-2">
                  <p className="text-sm text-gray-500"></p>
                </div>
                <div className="mt-4">
                  <div className={'columns mb-2 mt-2'}>
                    <div className={'columns-1'}>
                      <label className={'text-sm text-gray-700'}>Name</label>
                      <TextField></TextField>
                    </div>
                    <div className={'columns-1'}>
                      <label className={'text-sm text-gray-700'}>URL</label>
                      <TextField></TextField>
                    </div>
                    <div className={'columns-1'}>
                      <label className={'text-sm text-gray-700'}>API Key</label>
                      <TextField></TextField>
                    </div>
                    <div className={'flex py-4'}>
                      <Switch
                        checked={enabled}
                        onChange={setEnabled}
                        className={`${
                          enabled ? 'bg-blue-600' : 'bg-gray-200'
                        } relative inline-flex h-6 w-11 items-center rounded-full`}
                      >
                        <span
                          className={`${
                            enabled ? 'translate-x-6' : 'translate-x-1'
                          } inline-block h-4 w-4 transform rounded-full bg-white transition-transform`}
                        />
                      </Switch>
                      <label className={'text-sm text-gray-700 px-2'}>Enable</label>
                    </div>
                  </div>
                  <div></div>
                  <div className={'flex'}>
                    <div className={'flex-1'}>
                      <Button title={'Save'} onClick={closeModal}></Button>
                    </div>
                    <div className={'flex-2'}>
                      <Button title={'Cancel'} onClick={closeModal}></Button>
                    </div>
                  </div>
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </div>
      </Dialog>
    </Transition>
  );
};

Modal.propTypes = {
  isOpen: propTypes.bool.isRequired,
  closeModal: propTypes.func.isRequired,
  title: propTypes.string.isRequired,
};

export default Modal;
